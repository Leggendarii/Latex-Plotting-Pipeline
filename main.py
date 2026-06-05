import subprocess
import glob
import os

# Remove old PDF and auxiliary files
print("Cleaning old files...")
for pattern in ['figures/*.pdf', 'source_tex/*.aux', 'source_tex/*.log', 'figures/*.aux', 'figures/*.log']:
    for file in glob.glob(pattern):
        os.remove(file)

# Compile all .tex files
print("Compiling LaTeX files...")
for tex_file in glob.glob('source_tex/*.tex'):
    subprocess.run([
        'pdflatex',
        '-interaction=nonstopmode',
        '-output-directory=../figures',
        os.path.basename(tex_file)
    ], cwd='source_tex', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Clean auxiliary files
for ext in ['*.log', '*.aux']:
    for file in glob.glob(f'figures/{ext}'):
        os.remove(file)

print("Done!")
