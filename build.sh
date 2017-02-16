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

# build data (but not on travis)
if [ -z "$TRAVIS" ]; then
    echo "[build] building data"
    snakemake data
fi

# build manuscript
echo "[build] building manuscript"
snakemake manuscript
