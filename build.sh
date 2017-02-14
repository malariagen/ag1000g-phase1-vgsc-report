#!/bin/bash

# add texlive to the path
export PATH=./texlive/2016/bin/x86_64-linux:$PATH

# test 
tex --version
pdflatex main.tex

