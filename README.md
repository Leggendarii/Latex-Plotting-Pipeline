TEST PLOT PIPELINE - README
============================

PROJECT DESCRIPTION
-------------------
This project automates the workflow for generating artificial data 
and compiling LaTeX figures to PDF.


PROJECT STRUCTURE
-----------------
main.py              -- Main script that compiles .tex files to PDF and cleans auxiliary files
simulatuon.py        -- Script for generating artificial data (trigonometric functions)
data/                -- Folder containing data files (.csv)
figures/             -- Output folder with compiled PDFs
source_tex/          -- Folder containing LaTeX source files (.tex)


HOW TO USE
----------

Step 1: Generate Artificial Data
    python simulatuon.py

This creates a data/data.csv file containing 100 points with values of:
  - x: linear array from 0 to 10
  - sin: sine of x
  - cos: cosine of x


Step 2: Compile LaTeX Figures
    python main.py

This script:
  1. Cleans old PDF and auxiliary files
  2. Compiles all .tex files in the source_tex/ folder
  3. Generates PDFs in the figures/ folder
  4. Cleans auxiliary files generated during compilation


DEPENDENCIES
------------

Python Packages (install via pip):
  - numpy (for simulatuon.py)
  - pandas (for simulatuon.py)
  - main.py requires no external packages

System Applications (must be installed on your PC):
  - pdflatex (LaTeX compiler - part of MiKTeX or TeX Live distribution)
    Like Inkscape for SVG→PDF, pdflatex is an external system application
    that must be installed separately on your operating system.
  - MiKTeX or TeX Live distribution for Windows/Mac/Linux


PACKAGE INSTALLATION
--------------------
To install Python packages:
    pip install numpy pandas

To install pdflatex:
  - Windows: Download and install MiKTeX (https://miktex.org)
  - Mac: Install MacTeX or use Homebrew
  - Linux: Use your package manager (apt, yum, etc.)


OUTPUT
------
After execution:
  - Generated data is located in data/data.csv
  - Compiled PDFs are located in figures/
  - Auxiliary files (.aux, .log) are automatically removed


NOTES
-----
  - .tex files must be placed in the source_tex/ folder
  - The script automatically cleans old output before generating new files
  - To modify generated data, edit the simulatuon.py file
