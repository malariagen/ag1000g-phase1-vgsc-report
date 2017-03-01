
# These rules ensures any changes to setup or utility files will trigger
# a rebuild.

rule src:
    output:
        "src/python/zcache.py",
        "src/python/veff.py",
        "src/python/util.py",


rule setup:
    input:
        rules.src.output,
        "notebooks/setup.ipynb",
    output:
        "build/notebooks/setup.md",
    shell:
        "./nbexec.sh notebooks/setup.ipynb"


########
# Data #
########

# The rules in this section all require data from an external source
# (e.g., the Ag1000G FTP site, or VectorBase). N.B., these rules
# assume you have a local copy of the Ag1000G FTP site (at least the
# files needed). Because these rules need external data, they cannot
# be run during continuous integration checks.


# This rule is an example of how to include a Jupyter notebook in the
# data build. The notebook depends on some data from the Ag1000G FTP
# site.

rule data_demo:
    input:
        rules.setup.output,
        "notebooks/data_demo.ipynb",
    output:
        "build/notebooks/data_demo.md",
    shell:
        "./nbexec.sh notebooks/data_demo.ipynb"


# Extract data on VGSC variants.

rule data_variants_phase1:
    input:
        rules.setup.output,
        "notebooks/data_variants_phase1.ipynb",
    output:
        "build/notebooks/data_variants_phase1.md",
    shell:
        "./nbexec.sh notebooks/data_variants_phase1.ipynb"


# Phase multiallelics.

rule data_phase_multiallelics_phase1:
    input:
        rules.setup.output,
        "notebooks/data_phase_multiallelics_phase1.ipynb",
    output:
        "build/notebooks/data_phase_multiallelics_phase1.md",
    shell:
        "./nbexec.sh notebooks/data_phase_multiallelics_phase1.ipynb"


# This rule builds all data, indicating success by touching a flag
# file.

rule data:
    input:
        rules.data_demo.output,
        rules.data_variants_phase1.output,
        rules.data_phase_multiallelics_phase1.output,
        # add more inputs here as required
    output:
        touch("build/data.done")


###########
# Artwork #
###########

# The rules in this section build artwork (figures, figure components,
# etc.). N.B., These rules assume that any data required has been
# produced previously by the data build and is present in the 'data'
# folder and checked into the GitHub repo. 


# This rule is an example of how to include a Jupyter notebook in the
# artwork build.

rule artwork_demo:
    input:
        rules.setup.output,
        "notebooks/artwork_demo.ipynb",
    output:
        "build/notebooks/artwork_demo.md",
        "artwork/demo.png",
    shell:
        "./nbexec.sh notebooks/artwork_demo.ipynb"


# This rule builds all artwork.

rule artwork:
    input:
        rules.artwork_demo.output,
        # add more inputs here as required
    output:
        touch("build/artwork.done")


##########
# Tables #
##########

# The rules in this section build tables for the manuscript. N.B.,
# These rules assume that any data required has been produced
# previously by the data build and is present in the 'data' folder and
# checked into the GitHub repo.


# Demo of a notebook that builds a table for inclusion in the
# manuscript.

rule table_demo:
    input:
        rules.setup.output,
        "notebooks/table_demo.ipynb",
    output:
        "build/notebooks/table_demo.md",
        "tables/demo.tex"
    shell:
        "./nbexec.sh notebooks/table_demo.ipynb"


# Build the LaTex table of missense variants in VGSC.

rule table_variants_missense:
    input:
        rules.setup.output,
        "notebooks/table_variants_missense.ipynb",
        "data/missense_multiallelics.mvncall.200.npz",
        "data/tbl_variants_phase1.pkl",
    output:
        "build/notebooks/table_variants_missense.md",
        "tables/variants_missense.tex"
    shell:
        "./nbexec.sh notebooks/table_variants_missense.ipynb"


# This rule builds all tables.

rule tables:
    input:
        rules.table_demo.output,
        rules.table_variants_missense.output,
        # add more inputs here as required
    output:
        touch("build/tables.done")


##############
# Manuscript #
##############

# This rule builds the manuscript PDF file. It should depend on all
# the artwork and tables.

rule manuscript:
    input:
        rules.artwork.output,
        rules.tables.output,
        "main.tex",
        "refs.bib",
        # add more inputs here as required
    output:
        "build/main.pdf",
        touch("build/main.done")
    shell:
        "./latex.sh"


#########
# Clean #
#########


# This rule cleans out the build folder.

rule clean:
    shell:
        "rm -rvf build/*"
