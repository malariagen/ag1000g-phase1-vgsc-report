#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# setup environment
source env.sh

# build manuscript
echo "[build] building manuscript"
snakemake manuscript

# copy PDF back into version control
cp -v build/main.pdf manuscript
