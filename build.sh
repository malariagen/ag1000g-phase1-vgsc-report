#!/bin/bash

# ensure any errors cause build to fail
set -xeuo pipefail

# add texlive to the path
export PATH=./texlive/2016/bin/x86_64-linux:$PATH

# test latex
tex --version
pdflatex main.tex

