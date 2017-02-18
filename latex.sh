#!/bin/bash

set -eo pipefail

# setup environment
source env.sh

# run pdflatex + biber + pdflatex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
biber main
pdflatex -interaction=nonstopmode -halt-on-error main.tex

# copy out to build directory 
mkdir -pv build
cp -v main.pdf build
