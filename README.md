# agam-vgsc-report

## Contributor guide

**Step 1**: Fork this repository into your own GitHub account.

**Step 2**: Clone your fork to your local system. E.g.:

```bash
$ clone git@github.com:alimanfoo/agam-vgsc-report.git
$ cd agam-vgsc-report
$ git remote add upstream git@github.com:malariagen/agam-vgsc-report.git
```

**Step 3**: Install dependencies (TeX Live, Miniconda):

```bash
$ ./install.sh
```

**Step 4**: Verify you can build the manuscript:

```bash
$ ./build.sh
```

This should produce a file 'build/main.pdf'.

**Step 5**: Create a branch to work in, e.g.:

```bash
$ git checkout master
$ git pull
$ git fetch upstream
$ git rebase upstream/master
$ git push
$ git checkout -b edit-results-section
$ git push -u origin edit-results-section
```

**Step 6**: Do some work, then add, commit and push, e.g.:

```bash
$ # edit manuscript/main.tex
$ git add manuscript/main.tex
$ git commit -m 'corrected typo in results paragraph 1'
$ git push
```

**Step 7**: When the work is ready for review, make sure all changes
are committed and pushed up to your working branch, then check you can
build the manuscript locally:

```bash
$ ./build.sh
```

Then go to github.com and create a pull request from the branch on
your repository to malariagen/agam-vgsc-report master branch.

### Running a Jupyter notebook server

The install script will install Miniconda locally and create an
environment with various scientific Python packages installed. You can
activate this environment at any time, e.g.:

```bash
$ export PATH=./dependencies/miniconda/bin:$PATH
$ source activate agam-vgsc-report
(agam-vgsc-report) $ jupyter notebook &
```

If there are any Python packages you need to install, you will need to
add them to either 'config/conda.txt' if the packages can be installed
via conda, or 'config/pypi.txt' if the packages can only be installed
via pip.

