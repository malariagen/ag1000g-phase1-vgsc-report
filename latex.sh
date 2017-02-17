#!/bin/bash

set -eo pipefail

source env.sh
mkdir -pv build
cp -v manuscript/* build
pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error build/main.tex
biber build/main
pdflatex -output-directory=build -interaction=nonstopmode -halt-on-error build/main.tex
cp -v build/main.pdf manuscript
