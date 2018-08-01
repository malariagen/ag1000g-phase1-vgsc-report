# agam-vgsc-report

[![Build Status](https://travis-ci.org/malariagen/agam-vgsc-report.svg?branch=master)](https://travis-ci.org/malariagen/agam-vgsc-report)

This is a work in progress. It has not been reviewed, approved or endorsed by anyone. If you have 
any questions, please contact Alistair Miles (alimanfoo@googlemail.com) or Chris Clarkson (cc28@sanger.ac.uk).

## Contributor guide

### Getting started

The following steps describe how to set up a development environment for working on the manuscript 
and the supporting notebooks.

**Step 1**: Fork this repository into your own GitHub account.

**Step 2**: Clone your fork to your local system. E.g.:

```bash
$ git clone git@github.com:alimanfoo/agam-vgsc-report.git
$ cd agam-vgsc-report
$ git submodule update --init --recursive
$ git remote add upstream git@github.com:malariagen/agam-vgsc-report.git
```

...replacing 'alimanfoo' with your GitHub username.

**Step 3**: Install dependencies (Miniconda, TeXLive):

From the repo working directory, run:

```bash
$ ./agam-report-base/install/install-conda.sh
```

This will install Miniconda into the ``deps`` directory within the repository
root directory.

Then run:

```bash
$ ./agam-report-base/install/install-texlive.sh
```

This will install TexLive into the ``deps`` directory within the repository
root directory.

### Building the manuscript

To build the manuscript, from the repository root directory, run:

```bash
$ source env.sh
$ ./latex.sh
```

This should rebuild the file ``main.pdf``.

### Data dependencies

To build supporting data for the manuscript, you will need some files from the Ag1000G FTP site
copied to your local filesystem. The data build assumes you have a mirror of the necessary files
under a directory called ``ngs.sanger.ac.uk`` within the repository root directory.

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

...replacing "edit-results-section" with an appropriate branch name
for the work you want to do.

**Step 3**: Do some work, then add, commit and push, e.g.:

```bash
$ # edit main.tex
$ git add main.tex
$ git commit -m 'corrected typo in results paragraph 1'
$ git push
```

**Step 4**: When the work is ready for review, build the manuscript
locally:

```bash
$ source env.sh
$ ./latex.sh
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
environment with various scientific Python packages installed. To launch 
a Jupyter notebook server:

```bash
$ source env.sh
$ jupyter notebook
```




## Running the repo notebooks

Due to dependencies between the notebooks in this repository, if you would 
like to re-run the analyses from this projects you will need to download 
the Ag1000g phase1 data required from ftp then run the python notebooks 
within the "notebooks/" directory in the following sequence:


**run data notebooks first in the following order**

1. data_phasing_extra_phase1.ipynb - uses mvncall to phase two multiallelics 
and N1570Y SNP filtered out of PASS dataset.

2. data_combined_haplotypes.ipynb - combines the haplotype data with extras 
phased by mvncall.
 
3. data_variants_phase1.ipynb - extracts data on all VGSC mutations.

4. data_misc.ipynb - brings some small data files directly into Git repo.

5. table_variants_missense.ipynb


**run the following three artwork notebooks next in this order - they generate some data files used later**

6. artwork_hierarchical_cluster_vgsc.ipynb - perform hierarchical clustering 
based on technique used in Ag1000g Nature paper and produces figure.

7. artwork_median_joining_networks.ipynb - performs median joining network 
analysis and produces figures.

8. artwork_ehh_decay.ipynb - performs ehh analysis using hierarchical 
clustering haplotype clusters.


**once the above have been run the following notebooks can then be run in any order**

artwork_ld.ipynb - runs LD analysis and produces heatmap figure.

artwork_hapfreq_map.ipynb - generates network cluster map artwork.

artwork_assay_design.ipynb -  analyses number of SNPs required in genetic assay 
to define haplotype groups and generates figure.

analyse_Dxy_using_hierarchical_clusters.ipynb - analyses divergence between 
clusters and produces figures.

supp_tables.ipynb - generates supplementary data tables.

analyse_moving_haplotype_homozygosity.ipynb - does what it says on the tin.

table_variants_missense_display.ipynb - tables for LaTeX