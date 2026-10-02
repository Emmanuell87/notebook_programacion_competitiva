"""
Generador del Notebook de Programacion Competitiva.

Lee contents.txt, arma un .tex insertando cada archivo de code/ como
un \\subsection{} con su codigo dentro de un bloque lstlisting, y compila
el PDF final con pdflatex (dos pasadas, para que el indice quede bien).

Uso:
    python generate_pdf.py

Para agregar un algoritmo nuevo:
    1. Crea el archivo .py dentro de code/<categoria>/
    2. Agrega una linea en contents.txt bajo la seccion que corresponda:
       <categoria>/archivo.py<TAB>Titulo que va a aparecer en el PDF
    3. Vuelve a correr este script.
"""

import ast
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
CODE_DIR = BASE_DIR / "code"
CONTENTS_FILE = BASE_DIR / "contents.txt"
TEMPLATE_FILE = BASE_DIR / "notebook_template.tex"
OUTPUT_TEX = BASE_DIR / "notebook.tex"


def escapar_latex(texto):
    """Escapa los caracteres especiales de LaTeX en texto plano (titulos)."""
    reemplazos = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for viejo, nuevo in reemplazos.items():
        texto = texto.replace(viejo, nuevo)
    return texto


def parsear_contents(ruta):
    """
    Devuelve una lista de bloques:
      ("seccion", titulo)
      ("archivo", ruta_relativa, titulo_subseccion, es_mini)
    Deja de leer apenas encuentra una seccion llamada exactamente "Fin".

    titulo_subseccion puede ser:
      - un titulo normal -> crea un \\subsection{} numerado (aparece en el indice)
      - None -> el archivo continua la subseccion anterior, sin ningun
        encabezado (es_mini se ignora)
      - un titulo con es_mini=True -> el archivo continua la subseccion
        anterior pero con una etiqueta chica (sin numerar, no aparece en
        el indice), util para distinguir funciones dentro de un mismo
        grupo de archivos pegados (ej. Geometria computacional). Se arma
        con el prefijo "~" en contents.txt: "~nombre_funcion()".
    """
    bloques = []
    detenido = False

    with open(ruta, encoding="utf-8") as f:
        for num_linea, linea_cruda in enumerate(f, 1):
            if detenido:
                break

            linea = linea_cruda.split("#", 1)[0].rstrip("\n")
            if not linea.strip():
                continue

            if linea.strip().startswith("[") and linea.strip().endswith("]"):
                titulo = linea.strip()[1:-1].strip()
                if titulo == "Fin":
                    detenido = True
                    break
                bloques.append(("seccion", titulo))
                continue

            if "\t" not in linea:
                # sin TAB: es un archivo que continua la subseccion anterior
                # (muchos editores recortan el TAB final de una linea si no
                # hay texto despues, asi que esto cubre ese caso tambien)
                bloques.append(("archivo", linea.strip(), None, False))
                continue

            ruta_archivo, titulo_sub = linea.split("\t", 1)
            titulo_sub = titulo_sub.strip()
            # " :: texto" al final del titulo = complejidad (LaTeX tal cual)
            complejidad = None
            if " :: " in titulo_sub:
                titulo_sub, complejidad = [x.strip() for x in titulo_sub.split(" :: ", 1)]
            # titulo vacio o "-" = continuar en la misma subseccion anterior,
            # sin crear ningun encabezado (util cuando una subseccion del
            # documento principal mezcla formulas (.tex) y codigo (.py))
            if titulo_sub == "-" or not titulo_sub:
                bloques.append(("archivo", ruta_archivo.strip(), None, False, complejidad))
            elif titulo_sub.startswith("~"):
                # etiqueta chica sin numerar (ver docstring)
                bloques.append(("archivo", ruta_archivo.strip(), titulo_sub[1:].strip(), True, complejidad))
            else:
                bloques.append(("archivo", ruta_archivo.strip(), titulo_sub, False, complejidad))

    return bloques


MAX_LINEAS_EJEMPLO = 6
MARCA_INI_EJEMPLO = "# --- ejemplo ---"
MARCA_FIN_EJEMPLO = "# --- fin ejemplo ---"


def _fuente_ejemplo(texto, nodo, lineas):
    """Texto de una sentencia del bloque de pruebas: los assert se muestran
    como la expresion sola (sin 'assert' ni mensaje), con su comentario."""
    if isinstance(nodo, ast.Assert):
        expr = ast.get_source_segment(texto, nodo.test)
        resto = lineas[nodo.end_lineno - 1][nodo.end_col_offset:]
        return expr + resto
    return "\n".join(lineas[nodo.lineno - 1:nodo.end_lineno])


def extraer_ejemplo(codigo_completo):
    """Arma un ejemplo de uso a partir del bloque 'if __name__ == ...' de un
    archivo. Si el bloque tiene una region entre MARCA_INI_EJEMPLO y
    MARCA_FIN_EJEMPLO, se usa esa region completa. Si no, se toman
    sentencias simples (asignaciones, llamadas, assert) desde el principio,
    hasta el primer bucle/random/import o hasta MAX_LINEAS_EJEMPLO lineas.
    Los assert se muestran como la expresion sola. Devuelve None si no
    queda ningun assert."""
    marcador = '\nif __name__ == "__main__":'
    if marcador not in codigo_completo:
        return None
    cuerpo = codigo_completo.split(marcador, 1)[1]
    lineas = [l[4:] if l.startswith("    ") else l for l in cuerpo.splitlines()]

    explicito = False
    if MARCA_INI_EJEMPLO in lineas and MARCA_FIN_EJEMPLO in lineas:
        a = lineas.index(MARCA_INI_EJEMPLO)
        b = lineas.index(MARCA_FIN_EJEMPLO)
        lineas = lineas[a + 1:b]
        explicito = True

    texto = "\n".join(lineas)
    try:
        arbol = ast.parse(texto)
    except SyntaxError:
        return None

    salida = []
    largo_hasta_ultimo_assert = 0
    previo = 0  # ultima linea (1-indexada) ya consumida
    for nodo in arbol.body:
        if not explicito and not isinstance(nodo, (ast.Assign, ast.AnnAssign, ast.Expr, ast.Assert)):
            break
        if not explicito and any(
            isinstance(n, ast.Name) and n.id in ("random", "time") for n in ast.walk(nodo)
        ):
            break
        if isinstance(nodo, ast.Expr):
            llamada = nodo.value
            if isinstance(llamada, ast.Call) and isinstance(llamada.func, ast.Name) and llamada.func.id == "print":
                previo = nodo.end_lineno
                continue
        comentarios = [l for l in lineas[previo:nodo.lineno - 1] if l.strip().startswith("#")]
        fuente = _fuente_ejemplo(texto, nodo, lineas)
        bloque = comentarios + fuente.split("\n")
        if not explicito:
            # tope blando: se corta antes de pasarse, siempre que ya haya un assert
            if largo_hasta_ultimo_assert and len(salida) + len(bloque) > MAX_LINEAS_EJEMPLO:
                break
            if len(salida) + len(bloque) > MAX_LINEAS_EJEMPLO + 4:
                break
        salida.extend(bloque)
        previo = nodo.end_lineno
        if isinstance(nodo, ast.Assert):
            largo_hasta_ultimo_assert = len(salida)
    if not largo_hasta_ultimo_assert:
        return None
    # solo hasta el ultimo assert: sin preparativos ni comentarios sueltos
    salida = salida[:largo_hasta_ultimo_assert]
    return "\n".join(salida)


def construir_contenido_tex(bloques):
    # Sin needspace ni minipage: con frame=tb (solo linea arriba/abajo, sin
    # caja cerrada) un bloque SI puede partirse entre columnas o paginas
    # sin verse roto -- el corte no deja ningun rastro visual raro, asi
    # que no hace falta protegerlo ni reservarle espacio por adelantado.
    partes = []
    for bloque in bloques:
        if bloque[0] == "seccion":
            _, titulo = bloque
            partes.append(f"\\section{{{escapar_latex(titulo)}}}\n")
        else:
            _, ruta_rel, titulo_sub, es_mini, complejidad = bloque
            ruta_completa = CODE_DIR / ruta_rel

            if titulo_sub is not None:
                if es_mini:
                    # etiqueta chica sin numerar: distingue funciones
                    # dentro de un mismo grupo de archivos pegados, sin
                    # crear una entrada nueva en el indice.
                    partes.append(f"{{\\raggedright\\textit{{\\texttt{{{escapar_latex(titulo_sub)}}}}}\\par}}")
                else:
                    partes.append(f"\\subsection{{{escapar_latex(titulo_sub)}}}")
            if complejidad:
                partes.append(f"{{\\raggedright\\small\\textit{{Complejidad:}} {complejidad}\\par}}")

            if ruta_completa.suffix == ".tex":
                # contenido conceptual (formulas, texto) ya escrito en LaTeX: se inserta tal cual
                contenido = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                partes.append(contenido + "\n")
            else:
                # codigo: se envuelve en lstlisting con resaltado de sintaxis.
                completo = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                marcador = '\nif __name__ == "__main__":'
                codigo = completo.split(marcador)[0].rstrip("\n")

                partes.append("\\begin{lstlisting}[language=Python]")
                partes.append(codigo)
                partes.append("\\end{lstlisting}\n")

                # ejemplo de uso, sacado del bloque de pruebas del archivo
                ejemplo = extraer_ejemplo(completo)
                if ejemplo:
                    partes.append(
                        "\\begin{lstlisting}[language=Python,frame=none,numbers=none,"
                        "backgroundcolor=\\color{gray!12},aboveskip=0pt,belowskip=6pt]"
                    )
                    partes.append(ejemplo)
                    partes.append("\\end{lstlisting}\n")

    return "\n".join(partes)


def main():
    # Uso: python generate_pdf.py [archivo_contenido] [nombre_salida] [titulo]
    # Sin argumentos genera notebook.pdf desde contents.txt.
    contents_file = BASE_DIR / (sys.argv[1] if len(sys.argv) > 1 else "contents.txt")
    nombre = sys.argv[2] if len(sys.argv) > 2 else "notebook"
    titulo = sys.argv[3] if len(sys.argv) > 3 else "Notebook de Programación Competitiva"
    output_tex = BASE_DIR / f"{nombre}.tex"

    if not contents_file.exists():
        print(f"ERROR: no se encontro {contents_file}")
        sys.exit(1)

    bloques = parsear_contents(contents_file)
    contenido = construir_contenido_tex(bloques)

    plantilla = TEMPLATE_FILE.read_text(encoding="utf-8")
    if "%%CONTENIDO%%" not in plantilla:
        print(f"ERROR: {TEMPLATE_FILE} no tiene el marcador %%CONTENIDO%%")
        sys.exit(1)

    tex_final = plantilla.replace("%%CONTENIDO%%", contenido).replace("%%TITULO%%", titulo)
    output_tex.write_text(tex_final, encoding="utf-8")
    print(f"Generado: {output_tex}")

    for intento in (1, 2):
        resultado = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", output_tex.name],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",  # pdflatex puede cortar un caracter UTF-8 al partir lineas
        )
        if resultado.returncode != 0:
            print(f"ERROR compilando (pasada {intento}):")
            print(resultado.stdout[-3000:])
            sys.exit(1)

    print(f"PDF generado correctamente: {BASE_DIR / (nombre + '.pdf')}")


if __name__ == "__main__":
    main()
