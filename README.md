# Notebook de Programación Competitiva

Este repositorio contiene un notebook para competencias de programación (ICPC, CCPL, Codeforces, etc.). Incluye algoritmos y estructuras de datos organizados por categorías, listos para compilarse en un documento PDF de referencia.

---

## 📁 Estructura del Repositorio

* `code/`: Códigos fuente de los algoritmos (`.py`, `.cpp`, `.tex`, etc.) organizados por carpetas conceptuales.
* `contents.txt`: Archivo de índice que define las secciones y los algoritmos que aparecerán en el PDF.
* `notebook_template.tex`: Plantilla LaTeX base con la configuración de página y estilos.
* `generate_pdf.py`: Script de Python que construye el archivo `notebook.tex` y genera `notebook.pdf`.
* `.github/workflows/build-pdf.yml`: Acción de GitHub que compila automáticamente el PDF al subir cambios a `main` o `master`.

---

## 🛠️ Requisitos Previos (para compilar localmente)

1. **Python 3.x**
2. **Distribución LaTeX con `pdflatex`**:
   * **Windows:** [MiKTeX](https://miktex.org/) o TeX Live.
   * **Linux (Ubuntu/Debian):** `sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended`
   * **macOS:** [MacTeX](https://www.tug.org/mactex/)

---

## 🚀 Compilación Local

Para generar el PDF localmente, ejecuta en la terminal:

```bash
python generate_pdf.py
```

El script actualizará `notebook.tex` y generará `notebook.pdf`.

---

## ➕ Cómo Agregar un Nuevo Algoritmo

1. Guarda el código fuente en la subcarpeta correspondiente dentro de `code/` (ej. `code/06_grafos/dijkstra.py`).
2. Agrega una línea en `contents.txt` bajo la sección requerida usando la estructura:
   ```text
   06_grafos/dijkstra.py<TAB>Algoritmo de Dijkstra
   ```
3. Vuelve a ejecutar `python generate_pdf.py`.

---

## 🤖 Compilación Automática (GitHub Actions)

Dado que `notebook.pdf` no se sube directamente al control de versiones (Git), el flujo de GitHub Actions compilará automáticamente el documento cada vez que hagas `git push`. Podrás descargar el PDF compilado en la pestaña **Actions** de GitHub seleccionando la última ejecución realizada.
