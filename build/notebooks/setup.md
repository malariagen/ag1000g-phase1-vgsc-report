

```python
%%HTML
<style type="text/css">
.container {
    width: 100%;
}
#maintoolbar {
    display: none;
}
#header-container {
    display: none;
}
div#notebook {
    padding-top: 0;
}
</style>
```


<style type="text/css">
.container {
    width: 100%;
}
#maintoolbar {
    display: none;
}
#header-container {
    display: none;
}
div#notebook {
    padding-top: 0;
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
```


```python
# plotting setup
%matplotlib inline
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
# N.B., reduced font size
rcParams['font.size'] = 6
rcParams['axes.labelsize'] = 6
rcParams['xtick.labelsize'] = 6
rcParams['ytick.labelsize'] = 6
rcParams['legend.fontsize'] = 6
rcParams['axes.linewidth'] = .5
rcParams['lines.linewidth'] = .5
rcParams['patch.linewidth'] = .5
rcParams['ytick.direction'] = 'out'
rcParams['xtick.direction'] = 'out'
rcParams['savefig.jpeg_quality'] = 100
rcParams['lines.markeredgewidth'] = .5
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
import vcfnp
import anhima
import allel
```


```python
# ag1k imports
sys.path.insert(0, '../src/python')
from util import *
import zcache
import veff
```


```python
def geneset_to_pandas(geneset):
    """Life is a bit easier when a geneset is a pandas DataFrame."""
    items = []
    for n in geneset.dtype.names:
        v = geneset[n]
        # convert bytes columns to unicode (which pandas then converts to object)
        if v.dtype.kind == 'S':
            v = v.astype('U')
        items.append((n, v))
    return pandas.DataFrame.from_items(items)
```


```python
class SeqFeature(object):
    """Genomic sequence feature, with utilities for mapping between coordinate systems.

    Parameters
    ----------
    seqid : string
        Chromosome or contig.
    start : int
        Start coordinate, 1-based.
    end : int
        End coordinate, 1-based, end-inclusive.

    """
    
    def __init__(self, seqid, start, end, strand='+', genome=None):
        self.seqid = seqid
        self.start = start
        self.end = end
        self.strand = strand
        self.genome = genome
    
    @property
    def loc(self):
        """A zero-based stop-exclusive slice."""
        return slice(self.start - 1, self.end)
        
    @property
    def query(self):
        """A pandas-style query string."""
        return "(seqid == %r) & (start >= %s) & (end <= %s)" % (self.seqid, self.start, self.end)

    @property
    def region_str(self):
        """A samtools-style region string."""
        return "%s:%s-%s" % (self.seqid, self.start, self.end)
    
    @property
    def seq(self):
        """The reference sequence."""
        return self.genome[self.seqid][self.loc]
        
    def to_slice(self):
        """Convert to zero-based stop-exclusive slice. DEPRECATED: use loc property instead."""
        return slice(self.start - 1, self.end)
    
    def __len__(self):
        # include stard and end positions in length
        return self.end - self.start + 1
    
    def __iter__(self):
        yield self.seqid
        yield self.start
        yield self.end
        
```


```python

```
