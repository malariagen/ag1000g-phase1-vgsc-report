# Data
# ====
#
# This snakefile has rules to build required data files.
#
# The rules in this section all require data from an external source (e.g., the Ag1000G FTP site,
# or VectorBase). N.B., these rules assume you have a local copy of the Ag1000G FTP site (at least
# the files needed). Because these rules need external data, they cannot be run during continuous
# integration checks.
#

# Setup
# -----
#
# Rules in this section include source and setup scripts, to ensure any changes in these will
# trigger a rebuild.
#

rule src:
    # Python sources.
    output:
        "src/python/zcache.py",
        "src/python/veff.py",
        "src/python/util.py",

rule setup:
    # Setup notebook.
    input:
        rules.src.output,
        "notebooks/setup.ipynb",
    output:
        "build/notebooks/setup.md",
    shell:
        "./nbexec.sh notebooks/setup.ipynb"

# Data
# ----
#
# All data rules.
#

rule demo:
    # Example of how to include a Jupyter notebook in the data build. The notebook depends on some
    # data from the Ag1000G FTP site.
    input:
        rules.setup.output,
        "notebooks/data_demo.ipynb",
    output:
        "build/notebooks/data_demo.md",
        "data/demo.npy",
    shell:
        "./nbexec.sh notebooks/data_demo.ipynb"

rule variants_phase1:
    # Extract a table of data on VGSC variants.
    input:
        rules.setup.output,
        "notebooks/data_variants_phase1.ipynb",
    output:
        "build/notebooks/data_variants_phase1.md",
        "data/tbl_variants_phase1.pkl",
        "data/tbl_variants_phase1.txt",
    shell:
        "./nbexec.sh notebooks/data_variants_phase1.ipynb"

rule phase_multiallelics_phase1:
    # Phase multiallelics onto biallelic scaffold.
    input:
        rules.setup.output,
        "notebooks/data_phase_multiallelics_phase1.ipynb",
    output:
        "build/notebooks/data_phase_multiallelics_phase1.md",
        "data/missense_multiallelics.mvncall.50.npz",
        "data/missense_multiallelics.mvncall.100.npz",
        "data/missense_multiallelics.mvncall.200.npz",
    shell:
        "./nbexec.sh notebooks/data_phase_multiallelics_phase1.ipynb"

#
# Utilities
# ---------
#

rule all:
    # Build all data, indicating success by touching a flag file.
    input:
        rules.demo.output,
        rules.variants_phase1.output,
        rules.phase_multiallelics_phase1.output,
        # add more inputs here as required
    output:
        touch("build/data.done")
