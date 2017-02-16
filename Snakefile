# This rule builds the manuscript file. It depends on all the
# notebooks having run successfully.

rule manuscript:
    input:
        "manuscript/main.tex",
        "build/notebooks.done"
    output:
        "build/main.pdf"
    shell:
        "pdflatex -output-directory=build -interaction=errorstopmode -halt-on-error manuscript/main.tex"


# This rule is an example of how to include a Jupyter notebook in the
# build. This notebook does not require any data from outside the
# repository, so it can also be run during continuous integration
# checks. To make this happen, *do* include the executed notebook
# ("build/notebooks/demo.ipynb") in the rule output. *Do* also include
# in the rule output any other files produced by the notebook such as
# image files (e.g., "artwork/demo.png").

rule notebook_demo:
    input:
        "notebooks/demo.ipynb"
    output:
        "build/notebooks/demo.ipynb",
        "artwork/demo.png",
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/demo.ipynb"


# This rule is an example of how to include a Jupyter notebook in the
# build. This notebook *does* require data from outside the
# repository, so it *cannot* be run during continuous integration
# checks. To make this happen, *do* include any data files produced by
# the notebook that get checked in via git (e.g., "data/demo.npy") but
# *do not* include the executed notebook
# ("build/notebooks/data_demo.ipynb") in the rule output.

rule notebook_data_demo:
    input:
        "notebooks/data_demo.ipynb"
    output:
        "data/demo.npy"
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/data_demo.ipynb"


# This rule builds all notebooks, indicating success by touching a
# flag file.

rule notebooks:
    input:
        rules.notebook_demo.output,
        rules.notebook_data_demo.output,
    output:
        touch("build/notebooks.done")
