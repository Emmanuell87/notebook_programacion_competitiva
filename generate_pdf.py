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
      ("archivo", ruta_relativa, titulo_subseccion)
    Deja de leer apenas encuentra una seccion llamada exactamente "Fin".
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
                bloques.append(("archivo", linea.strip(), None))
                continue

            ruta_archivo, titulo_sub = linea.split("\t", 1)
            titulo_sub = titulo_sub.strip()
            # titulo vacio o "-" = continuar en la misma subseccion anterior,
            # sin crear un encabezado nuevo (util cuando una subseccion
            # del documento principal mezcla formulas (.tex) y codigo (.py))
            if titulo_sub == "-":
                titulo_sub = ""
            bloques.append(("archivo", ruta_archivo.strip(), titulo_sub or None))

    return bloques


def calcular_espacio_archivo(ruta_rel, titulo_sub):
    """Calcula cuantas unidades de \\baselineskip ocupa un bloque de
    archivo (encabezado opcional + "Archivo:" + codigo/formula), para
    reservarle espacio con \\needspace antes de empezarlo."""
    ruta_completa = CODE_DIR / ruta_rel
    if not ruta_completa.exists():
        print(f"ERROR: no existe el archivo referenciado: {ruta_completa}")
        sys.exit(1)

    if ruta_completa.suffix == ".tex":
        # no tenemos forma barata de medir cuanto ocupa una formula/tabla
        # renderizada; usamos un valor fijo conservador
        return 6.0

    codigo = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
    marcador = '\nif __name__ == "__main__":'
    if marcador in codigo:
        codigo = codigo.split(marcador)[0].rstrip("\n")
    num_lineas = codigo.count("\n") + 1
    # El codigo se tipea en \scriptsize (lineas ~0.65x mas bajas que el
    # \baselineskip del texto normal, que es el que usa \needspace), por
    # eso el factor 0.65. extra = subtitulo + "Archivo:" + margen del frame.
    extra = 4.0 if titulo_sub is not None else 2.0
    return num_lineas * 0.65 + extra


def construir_contenido_tex(bloques):
    partes = []
    for idx, bloque in enumerate(bloques):
        if bloque[0] == "seccion":
            _, titulo = bloque
            # NO se fuerza salto de pagina aqui (\clearpage desperdiciaba
            # media pagina en blanco cada vez). En cambio, se reserva el
            # espacio del titulo DE SECCION MAS el del bloque que le sigue
            # inmediatamente (hasta un tope), para que el titulo nunca
            # quede solo al final de una pagina sin nada de contenido
            # debajo -- si no cabe ese combo, salta junto a la siguiente.
            espacio_siguiente = 0.0
            if idx + 1 < len(bloques) and bloques[idx + 1][0] == "archivo":
                _, ruta_sig, titulo_sig = bloques[idx + 1]
                espacio_siguiente = min(calcular_espacio_archivo(ruta_sig, titulo_sig), 20.0)
            espacio = 6.0 + espacio_siguiente
            partes.append(f"\\needspace{{{espacio:.1f}\\baselineskip}}\n\\section{{{escapar_latex(titulo)}}}\n")
        else:
            _, ruta_rel, titulo_sub = bloque
            ruta_completa = CODE_DIR / ruta_rel

            if ruta_completa.suffix == ".tex":
                # contenido conceptual (formulas, texto) ya escrito en LaTeX: se inserta tal cual
                if titulo_sub is not None:
                    partes.append(f"\\subsection{{{escapar_latex(titulo_sub)}}}")
                contenido = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                partes.append(contenido + "\n")
            else:
                # codigo: se envuelve en lstlisting con resaltado de sintaxis.
                # Reserva espacio vertical para todo el bloque (encabezado +
                # "Archivo:" + el codigo completo) ANTES de empezarlo, para
                # que si no cabe entero en lo que queda de la pagina, salte
                # de pagina completo en vez de partirse dejando 1-2 lineas
                # huerfanas al principio de la siguiente pagina.
                codigo = ruta_completa.read_text(encoding="utf-8").rstrip("\n")
                marcador = '\nif __name__ == "__main__":'
                if marcador in codigo:
                    codigo = codigo.split(marcador)[0].rstrip("\n")

                espacio = calcular_espacio_archivo(ruta_rel, titulo_sub)
                partes.append(f"\\needspace{{{espacio:.1f}\\baselineskip}}")

                if titulo_sub is not None:
                    partes.append(f"\\subsection{{{escapar_latex(titulo_sub)}}}")
                partes.append(f"\\textit{{Archivo: \\texttt{{{escapar_latex(ruta_rel)}}}}}")
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
