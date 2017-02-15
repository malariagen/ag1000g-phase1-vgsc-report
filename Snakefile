rule all:
    input:
        "build/main.pdf"

rule manuscript:
    input:
        "manuscript/main.tex",
        "build/notebooks.done"
    output:
        "build/main.pdf"
    shell:
        "pdflatex -output-directory=build -interaction=errorstopmode -halt-on-error manuscript/main.tex"

rule notebook_demo:
    input:
        "notebooks/demo.ipynb"
    output:
        "build/notebooks/demo.ipynb"
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/demo.ipynb"

rule notebooks:
    input:
        rules.notebook_demo.output
    output:
        touch("build/notebooks.done")

