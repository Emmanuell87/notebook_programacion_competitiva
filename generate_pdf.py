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
            # titulo vacio o "-" = continuar en la misma subseccion anterior,
            # sin crear ningun encabezado (util cuando una subseccion del
            # documento principal mezcla formulas (.tex) y codigo (.py))
            if titulo_sub == "-" or not titulo_sub:
                bloques.append(("archivo", ruta_archivo.strip(), None, False))
            elif titulo_sub.startswith("~"):
                # etiqueta chica sin numerar (ver docstring)
                bloques.append(("archivo", ruta_archivo.strip(), titulo_sub[1:].strip(), True))
            else:
                bloques.append(("archivo", ruta_archivo.strip(), titulo_sub, False))

    return bloques


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
            _, ruta_rel, titulo_sub, es_mini = bloque
            ruta_completa = CODE_DIR / ruta_rel

            if titulo_sub is not None:
                if es_mini:
                    # etiqueta chica sin numerar: distingue funciones
                    # dentro de un mismo grupo de archivos pegados, sin
                    # crear una entrada nueva en el indice.
                    partes.append(f"\\textit{{\\texttt{{{escapar_latex(titulo_sub)}}}}}")
                else:
                    partes.append(f"\\subsection{{{escapar_latex(titulo_sub)}}}")

            if ruta_completa.suffix == ".tex":
                # contenido conceptual (formulas, texto) ya escrito en LaTeX: se inserta tal cual
                contenido = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                partes.append(contenido + "\n")
            else:
                # codigo: se envuelve en lstlisting con resaltado de sintaxis.
                codigo = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                marcador = '\nif __name__ == "__main__":'
                if marcador in codigo:
                    codigo = codigo.split(marcador)[0].rstrip("\n")

                partes.append("\\begin{lstlisting}[language=Python]")
                partes.append(codigo)
                partes.append("\\end{lstlisting}\n")

    return "\n".join(partes)


def main():
    if not CONTENTS_FILE.exists():
        print(f"ERROR: no se encontro {CONTENTS_FILE}")
        sys.exit(1)

    bloques = parsear_contents(CONTENTS_FILE)
    contenido = construir_contenido_tex(bloques)

    plantilla = TEMPLATE_FILE.read_text(encoding="utf-8")
    if "%%CONTENIDO%%" not in plantilla:
        print(f"ERROR: {TEMPLATE_FILE} no tiene el marcador %%CONTENIDO%%")
        sys.exit(1)

    tex_final = plantilla.replace("%%CONTENIDO%%", contenido)
    OUTPUT_TEX.write_text(tex_final, encoding="utf-8")
    print(f"Generado: {OUTPUT_TEX}")

    for intento in (1, 2):
        resultado = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", OUTPUT_TEX.name],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
        )
        if resultado.returncode != 0:
            print(f"ERROR compilando (pasada {intento}):")
            print(resultado.stdout[-3000:])
            sys.exit(1)

    print(f"PDF generado correctamente: {BASE_DIR / 'notebook.pdf'}")


if __name__ == "__main__":
    main()
