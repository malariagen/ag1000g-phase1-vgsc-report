#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# add texlive to the path
export PATH=./dependencies/texlive/2016/bin/x86_64-linux:$PATH

# ensure build directory exists
mkdir -pv build

# build
snakemake all

