
# This rule ensures any changes to setup or utility files will trigger
# a rebuild.

rule py_setup:
    output:
        "src/python/zcache.py",
        "src/python/veff.py",
        "src/python/ag1k/phase1_ar3.py",
        "src/python/ag1k/phase1_ar31.py",
        "src/python/ag1k/phase2_ar1.py",
        "src/python/ag1k/util.py",
        "notebooks/setup.ipynb",
    

# This rule is an example of how to include a Jupyter notebook in the
# build. This notebook does not require any data from outside the
# repository, so it can also be run during continuous integration
# checks.

rule notebook_demo:
    input:
        rules.py_setup.output,
        "notebooks/demo.ipynb",
    output:
        "build/notebooks/demo.ipynb",
        "artwork/demo.png",
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/demo.ipynb"


# This rule is an example of how to include a Jupyter notebook in the
# build. This notebook requires data from outside the repository, so
# it cannot be run during continuous integration checks.

rule data_demo:
    input:
        rules.py_setup.output,
        "notebooks/data_demo.ipynb",
    output:
        "build/notebooks/data_demo.ipynb",
        "data/demo.npy"
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/data_demo.ipynb"


# This rule builds all data, indicating success by touching a
# flag file.

rule data:
    input:
        rules.data_demo.output,
	# add more inputs here
    output:
        touch("build/data.done")


# This rule builds all notebooks, indicating success by touching a
# flag file.

rule notebooks:
    input:
        rules.notebook_demo.output,
	# add more inputs here
    output:
        touch("build/notebooks.done")


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
