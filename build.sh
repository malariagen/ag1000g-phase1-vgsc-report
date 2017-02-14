#!/bin/bash

# ensure any errors cause build to fail
set -xeuo pipefail

# add texlive to the path
export PATH=./dependencies/texlive/2016/bin/x86_64-linux:$PATH

# test latex
tex --version
pdflatex main.tex

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# test miniconda
source activate scipy
python -c 'import sys; print(sys.version_info); import numpy; print(numpy.__version)'
