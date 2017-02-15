#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# add texlive to the path
export PATH=./dependencies/texlive/2016/bin/x86_64-linux:$PATH

# ensure build directory exists
mkdir -pv build

# activate conda environment
source activate agam-vgsc-report

# build
snakemake all

# copy manuscript file
if [[ -n "$TRAVIS_PULL_REQUEST" && "$TRAVIS_PULL_REQUEST" -ne "false" ]]; then 
    cp -v build/main.pdf build/main.PR.${TRAVIS_PULL_REQUEST}.pdf
fi
