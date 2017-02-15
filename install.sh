#!/bin/bash

# ensure script errors if any command fails
set -eo pipefail

# descend into dependencies directory
mkdir -pv dependencies
cd dependencies

# install texlive
if [ ! -f texlive.installed ]; then
    echo "[install] installing texlive"

    # clean up any previous
    rm -rvf texlive

    # download texlive
    wget --no-clobber ftp://tug.org/historic/systems/texlive/2016/install-tl-unx.tar.gz

    # unpack archive
    tar zxvf install-tl-unx.tar.gz

    # run installation
    ./install-tl-20160523/install-tl --profile=../config/texlive.profile

    # install additional packages
    export PATH=./texlive/2016/bin/x86_64-linux:$PATH
    tlmgr install csquotes
    tlmgr install biblatex
    tlmgr install logreq
    tlmgr install xstring
    tlmgr install adjustbox
    tlmgr install collectbox
    tlmgr install todonotes
    tlmgr install siunitx

    # mark successful installation
    touch texlive.installed

else
    echo "[install] skipping texlive installation"
fi

# install miniconda
if [ ! -f miniconda.installed ]; then
    echo "[install] installing miniconda"

    # clean up any previous
    rm -rvf miniconda

    # download miniconda
    wget --no-clobber https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

    # install miniconda
    bash Miniconda3-latest-Linux-x86_64.sh -b -p miniconda
    export PATH=./miniconda/bin:$PATH
    conda upgrade --yes conda

    # create default scientific Python environment
    conda config --add channels bioconda
    conda config --add channels conda-forge
    conda create --yes --name=agam-vgsc-report python=3.5
    source activate agam-vgsc-report
    conda install --yes --file ../config/conda.txt
    pip install -r ../config/pypi.txt

    # clean conda caches
    conda clean --yes --all

    # mark success
    touch miniconda.installed

else
    echo "[install] skipping miniconda installation"
fi

# check to see how much space needed for cache
du -hs ./*
du -hs ./*/*
