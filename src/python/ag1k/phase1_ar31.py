"""
This module contains convenience variables relating to the Ag1000G phase 1 AR3.1 data release.

Use this module in notebooks and scripts as follows:

    >>> import sys
    >>> sys.path.insert(0, '/path/to/malariagen/ag1000g/src/python')
    >>> from ag1k import phase1_ar31

"""
from __future__ import absolute_import, print_function, division


# standard library imports
import os


# third party library imports
import zarr
import petl as etl
import pandas
import h5py


# fundamentals
##############

title = 'Phase 1 AR3.1 release'
release_dir = '/kwiat/vector/ag1000g/release/phase1.AR3.1'


# variation
###########

variation_dir = os.path.join(release_dir, 'variation')

# main callset
callset_zarr_fn = os.path.join(variation_dir, 'main', 'zarr2', 'ag1000g.phase1.ar3')
if os.path.exists(callset_zarr_fn):
    callset = zarr.open_group(callset_zarr_fn, mode='r')

# main callset, PASS variants only
callset_pass_zarr_fn = os.path.join(variation_dir, 'main', 'zarr2', 'ag1000g.phase1.ar3.pass')
if os.path.exists(callset_pass_zarr_fn):
    callset_pass = zarr.open_group(callset_pass_zarr_fn, mode='r')


# haplotypes
############

haplotypes_dir = os.path.join(release_dir, 'haplotypes')

# try HDF5 first
callset_phased_h5_fn = os.path.join(haplotypes_dir, 'main', 'hdf5',
                                    'ag1000g.phase1.ar3.1.haplotypes.h5')
if os.path.exists(callset_phased_h5_fn):
    callset_phased = h5py.File(callset_phased_h5_fn, mode='r')

# prefer Zarr if available
callset_phased_zarr_fn = os.path.join(haplotypes_dir, 'main', 'zarr2',
                                      'ag1000g.phase1.ar3.1.haplotypes')
if os.path.exists(callset_phased_zarr_fn):
    callset_phased = zarr.open_group(callset_phased_zarr_fn, mode='r')

# haplotypes metadata
haplotypes_fn = os.path.join(haplotypes_dir, 'haplotypes.meta.txt')
if os.path.exists(haplotypes_fn):
    tbl_haplotypes = (
        etl
        .fromtsv(haplotypes_fn)
        .convert(('index', 'kt_2la', 'kt_2rb'), int)
    )
    lkp_haplotypes = tbl_haplotypes.recordlookupone('label')
    haplotypes = pandas.read_csv(haplotypes_fn, sep='\t', index_col='index')
