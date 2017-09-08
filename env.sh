#!/bin/bash

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# add texlive to the path
export PATH=./dependencies/texlive/bin/x86_64-linux:$PATH

# ensure build directory exists
mkdir -pv build

# activate conda environment
source activate agam-report-base
