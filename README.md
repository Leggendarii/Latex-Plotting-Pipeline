TEST PLOT PIPELINE - README
============================

DESCRIZIONE DEL PROGETTO
------------------------
Questo progetto automatizza il flusso di lavoro per la generazione di dati artificiali 
e la compilazione di figure LaTeX in PDF.


STRUTTURA DEL PROGETTO
---------------------
main.py              -- Script principale che compila i file .tex in PDF e pulisce i file ausiliari
simulatuon.py        -- Script per generare dati artificiali (funzioni trigonometriche)
data/                -- Cartella contenente i file di dati (.csv)
figures/             -- Cartella di output con i PDF compilati
source_tex/          -- Cartella contenente i file sorgente LaTeX (.tex)


COME UTILIZZARE
---------------

Passo 1: Generare i Dati Artificiali
    python simulatuon.py

Questo crea un file data/data.csv contenente 100 punti con i valori di:
  - x: array lineare da 0 a 10
  - sin: seno di x
  - cos: coseno di x


Passo 2: Compilare le Figure LaTeX
    python main.py

Questo script:
  1. Pulisce i vecchi file PDF e ausiliari
  2. Compila tutti i file .tex della cartella source_tex/
  3. Genera i PDF nella cartella figures/
  4. Pulisce i file ausiliari generati durante la compilazione


DIPENDENZE
----------

Python Packages:
  - numpy (per simulatuon.py)
  - pandas (per simulatuon.py)
  - main.py non richiede pacchetti esterni

Requisiti Esterni:
  - pdflatex (compiler LaTeX, deve essere installato nel sistema)


INSTALLAZIONE DEI PACCHETTI
---------------------------
pip install numpy pandas


OUTPUT
------
Al termine dell'esecuzione:
  - I dati generati si trovano in data/data.csv
  - I PDF compilati si trovano in figures/
  - I file ausiliari (.aux, .log) vengono automaticamente rimossi


NOTE
----
  - I file .tex devono essere posizionati nella cartella source_tex/
  - Lo script pulisce automaticamente i vecchi output prima di generare i nuovi
  - Per modificare i dati generati, edita il file simulatuon.py
