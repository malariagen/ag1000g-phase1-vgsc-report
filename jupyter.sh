#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# setup environment
source env.sh

# run jupyter notebook server
jupyter notebook
