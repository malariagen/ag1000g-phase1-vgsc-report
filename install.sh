#!/bin/bash

# ensure script errors if any command fails
set -xeuo pipefail

# install texlive
if [ ! -f texlive/installed ]; then
    echo "[install] installing texlive"
    # clean up any previous
    rm -rvf texlive
    # create directory for texlive
    mkdir -pv texlive
    cd texlive
    # download texlive
    wget ftp://tug.org/historic/systems/texlive/2016/install-tl-unx.tar.gz
    # unpack archive
    tar zxvf install-tl-unx.tar.gz
    # run installation
    ./install-tl-20160523/install-tl --profile=../texlive.profile
    # mark successful installation
    touch ./installed
    cd ..
else
    echo "[install] skipping texlive installation"
fi
