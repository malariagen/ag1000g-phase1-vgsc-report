#!/bin/bash

# ensure any errors cause build to fail
set -eo pipefail

# setup environment
source env.sh

# run notebook
jupyter nbconvert --execute --ExecutePreprocessor.timeout=1000 --output-dir=build/notebooks --to=markdown $1
