#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# add miniconda to the path
export PATH=./dependencies/miniconda/bin:$PATH

# activate conda environment
source activate agam-vgsc-report

# run jupyter notebook server
jupyter notebook 
