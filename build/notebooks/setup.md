

```python
%%HTML
<style type="text/css">
.container {
    width: 100%;
}
div#notebook {
    padding-top: 1em;
}
#header-container {
    display: none;
}
#header-bar {
    display: none;
}
#maintoolbar {
    display: none;
}
#menubar-container {
    position: fixed;
    margin-top: 0;
}
#site {
    height: auto !important;
}
</style>
```


<style type="text/css">
.container {
    width: 100%;
}
div#notebook {
    padding-top: 1em;
}
#header-container {
    display: none;
}
#header-bar {
    display: none;
}
#maintoolbar {
    display: none;
}
#menubar-container {
    position: fixed;
    margin-top: 0;
}
#site {
    height: auto !important;
}
</style>



```python
# python standard library
import sys
import os
import operator
import itertools
import collections
import functools
import glob
import csv
import datetime
import bisect
import sqlite3
import subprocess
import random
import gc
import shutil
import shelve
import contextlib
import tempfile
import math
import pickle
```


```python
# general purpose third party packages

import cython
%reload_ext Cython

import numpy as np
nnz = np.count_nonzero
import scipy
import scipy.stats
import scipy.spatial.distance
import numexpr
import h5py
import tables
import bcolz
import dask
import dask.array as da
import pandas
import IPython
from IPython.display import clear_output, display, HTML
import sklearn
import sklearn.decomposition
import sklearn.manifold
import petl as etl
etl.config.display_index_header = True
import humanize
from humanize import naturalsize, intcomma, intword
import zarr
import graphviz
import statsmodels.formula.api as sfa
```


```python
# plotting setup
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.gridspec import GridSpec
import matplotlib_venn as venn
import seaborn as sns
sns.set_context('paper')
sns.set_style('white')
sns.set_style('ticks')
rcParams = plt.rcParams
base_font_size = 8
rcParams['font.size'] = base_font_size
rcParams['axes.titlesize'] = base_font_size
rcParams['axes.labelsize'] = base_font_size
rcParams['xtick.labelsize'] = base_font_size
rcParams['ytick.labelsize'] = base_font_size
rcParams['legend.fontsize'] = base_font_size
rcParams['axes.linewidth'] = .5
rcParams['lines.linewidth'] = .5
rcParams['patch.linewidth'] = .5
rcParams['ytick.direction'] = 'out'
rcParams['xtick.direction'] = 'out'
rcParams['savefig.jpeg_quality'] = 100
rcParams['lines.markeredgewidth'] = .5
rcParams['figure.max_open_warning'] = 1000
```


```python
# bio third party packages
import Bio
import pyfasta
import pysam
import pysamstats
import petlx
import petlx.bio
import vcf
import anhima
import allel
```


```python
sys.path.insert(0, '../agam-report-base/src/python')
from util import *
import zcache
import veff
# import hapclust
ag1k_dir = '../ngs.sanger.ac.uk/production/ag1000g'
from ag1k import phase1_ar3
phase1_ar3.init(os.path.join(ag1k_dir, 'phase1', 'AR3'))
from ag1k import phase1_ar31
phase1_ar31.init(os.path.join(ag1k_dir, 'phase1', 'AR3.1'))
from ag1k import phase2_ar1
phase2_ar1.init(os.path.join(ag1k_dir, 'phase2', 'AR1'))
region_vgsc = SeqFeature('2L', 2358158, 2431617, label='Vgsc')

```
