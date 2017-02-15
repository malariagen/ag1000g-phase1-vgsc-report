#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# add texlive to the path
export PATH=./dependencies/texlive/2016/bin/x86_64-linux:$PATH

# build
snakemake all

# test latex
#tex --version
#pdflatex main.tex

# test miniconda
#source activate scipy
#python -c 'import sys; print(sys.version_info); import numpy; print(numpy.__version__)'
