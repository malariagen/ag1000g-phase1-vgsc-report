
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

rule artwork_demo:
    input:
        rules.py_setup.output,
        "notebooks/artwork_demo.ipynb",
    output:
        "build/notebooks/artwork_demo.ipynb",
        "artwork/demo.png",
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/artwork_demo.ipynb"


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


# Demo of a notebook that builds a table for inclusion in the
# manuscript.

rule table_demo:
    input:
        rules.py_setup.output,
        "notebooks/table_demo.ipynb",
    output:
        "build/notebooks/table_demo.ipynb",
        "manuscript/table.tex"
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/table_demo.ipynb"


# Run the notebook extracting information about VGSC variants.

rule data_variants_phase1:
    input:
        rules.py_setup.output,
        "notebooks/data_variants_phase1.ipynb",
    output:
        "build/notebooks/data_variants_phase1.ipynb",
        "data/tbl_variants_phase1.pkl",
        "data/tbl_variants_phase1.txt",
        "data/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.gff3.gz",
        "data/davies_vgsc_model_20170125.gff3",
    shell:
        "jupyter nbconvert --execute --ExecutePreprocessor.timeout=1000 --output-dir=build/notebooks --to=notebook notebooks/data_variants_phase1.ipynb"


# Run the notebook generating the LaTex table of missense variants.

rule table_variants_missense:
    input:
        rules.py_setup.output,
        "notebooks/table_variants_missense.ipynb",
    output:
        "build/notebooks/table_variants_missense.ipynb",
        "manuscript/table_variants_missense.tex"
    shell:
        "jupyter nbconvert --execute --output-dir=build/notebooks --to=notebook notebooks/table_variants_missense.ipynb"


# This rule builds all data, indicating success by touching a
# flag file.

rule data:
    input:
        rules.data_demo.output,
        rules.data_variants_phase1.output,
        # add more inputs here
    output:
        touch("build/data.done")


# This rule builds all notebooks, indicating success by touching a
# flag file.

rule notebooks:
    input:
        rules.artwork_demo.output,
        rules.table_demo.output,
        rules.table_variants_missense.output,
        # add more inputs here
    output:
        touch("build/notebooks.done")


# This rule builds the manuscript file. It depends on all the
# notebooks having run successfully.

rule manuscript:
    input:
        "manuscript/main.tex",
        rules.notebooks.output,
    output:
        "build/main.pdf"
    shell:
        "pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error manuscript/main.tex"
