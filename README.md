# agam-vgsc-report

[![Build Status](https://travis-ci.org/malariagen/agam-vgsc-report.svg?branch=master)](https://travis-ci.org/malariagen/agam-vgsc-report)

## Contributor guide

### Getting started

The following steps describe how to set up a development environment for working on the manuscript 
and the supporting notebooks.

**Step 1**: Fork this repository into your own GitHub account.

**Step 2**: Clone your fork to your local system. E.g.:

```bash
$ clone git@github.com:alimanfoo/agam-vgsc-report.git
$ cd agam-vgsc-report
$ git remote add upstream git@github.com:malariagen/agam-vgsc-report.git
```

...replacing 'alimanfoo' with your GitHub username.

**Step 3**: Install dependencies (TeX Live, Miniconda):

```bash
$ ./install.sh
```

This will install Tex Live and Miniconda into the ``dependencies`` directory within the repository
root directory.

### Building the manuscript

To build the manuscript, from the repository root directory, run:

```bash
$ ./build.sh
```

This should rebuild the file ``manuscript/main.pdf``, also running any supporting notebooks as 
required.

### Building the data

To build supporting data for the manuscript, you will need some files from the Ag1000G FTP site
copied to your local filesystem. The data build assumes you have a mirror of the necessary files
under a directory called ``ngs.sanger.ac.uk`` within the repository root directory.

If you have the necessary files mirrored locally, you can run:

```bash
$ source env.sh
(agam-vgsc-report) $ snakemake data
```

### Working on the manuscript

The following steps describe how to do some work on the manuscript and contribute the work back to
the MalariaGEN (upstream) repository.

**Step 1**: Make sure your master branch is synchronized with upstream master:

```bash
$ git checkout master
$ git pull
$ git fetch upstream
$ git rebase upstream/master
$ git push
```

**Step 2**: Create a branch to put your work in, e.g.:

```bash
$ git checkout -b edit-results-section
$ git push -u origin edit-results-section
```

**Step 3**: Do some work, then add, commit and push, e.g.:

```bash
$ # edit manuscript/main.tex
$ git add manuscript/main.tex
$ git commit -m 'corrected typo in results paragraph 1'
$ git push
```

**Step 4**: When the work is ready for review, check you can
build the manuscript locally:

```bash
$ ./build.sh
```

Then make sure all local changes are committed and pushed up to 
your remote branch:

```bash
$ git status
$ # if anything to commit...
$ git commit -a -m 'rebuild'
$ git push
```

Then go to github.com and [create a pull request](https://github.com/malariagen/agam-vgsc-report/compare) 
from the branch on your repository to malariagen/agam-vgsc-report master branch.

### Running a Jupyter notebook server

The install script will install Miniconda locally and create an
environment with various scientific Python packages installed. There is
a convenience script to launch a Jupyter notebook server:

```bash
$ ./jupyter.sh
```

Alternatively you can manually activate the conda environment and run jupyter, e.g.:

```bash
$ source env.sh
(agam-vgsc-report) $ jupyter notebook
```

### Installing LaTeX packages

If there are any LaTeX packages you need to install, edit the ``install.sh`` script by adding 
another ``tlmgr install ...`` command. Then rerun ``install.sh``.


### Installing Python packages

If there are any Python packages you need to install, add them to either 
``config/conda.txt`` if the packages can be installed via conda, or ``config/pypi.txt`` if the 
packages can only be installed via pip. Then rerun ``install.sh``.
