# -*- coding: utf-8 -*-
"""
This module contains convenience variables relating to the Ag1000G phase 2 AR1 data release.

Use this module in notebooks and scripts as follows:

    >>> import sys
    >>> sys.path.insert(0, '/path/to/malariagen/ag1000g/src/python')
    >>> from ag1k import phase2_ar1

"""
from __future__ import absolute_import, print_function, division


# standard library imports
import os


# third party library imports
import pyfasta
import allel
import petl as etl
import petlx
import petlx.bio
import h5py
import seaborn as sns
import pandas
import zarr


# fundamentals
##############

title = 'Phase 2 AR1 release'
release_dir = '/kwiat/vector/ag1000g/release/phase2.AR1'


# reference sequence
####################

chromosomes = '2R', '2L', '3R', '3L', 'X', 'Y_unplaced', 'UNKN'
autosomes = chromosomes[:4]
genome_dir = os.path.join(release_dir, 'genome')
genome_agamp3_dir = os.path.join(genome_dir, 'agamP3')
genome_agamp3_fn = os.path.join(genome_agamp3_dir, 'Anopheles-gambiae-PEST_CHROMOSOMES_AgamP3.fa')
if os.path.exists(genome_agamp3_fn):
    genome_agamp3 = pyfasta.Fasta(genome_agamp3_fn, key_fn=lambda v: v.split()[0])
genome_agamp4_dir = os.path.join(genome_dir, 'agamP4')
genome_agamp4_fn = os.path.join(genome_agamp4_dir, 'Anopheles-gambiae-PEST_CHROMOSOMES_AgamP4.fa')
if os.path.exists(genome_agamp4_fn):
    genome_agamp4 = pyfasta.Fasta(genome_agamp4_fn, key_fn=lambda v: v.split()[0])


# genome annotations
####################

geneset_dir = os.path.join(release_dir, 'geneset')
geneset_agamp42_fn = os.path.join(geneset_dir, 'Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.2.sorted.gff3.gz')
geneset_agamp44_fn = os.path.join(geneset_dir, 'Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.sorted.gff3.gz')


def load_geneset_agamp42(attributes=None):
    """Function to load data from GFF into a structured array. Can take a few seconds so put this
    into a function so user can decide whether to execute."""
    global geneset_agamp42
    geneset_agamp42 = allel.FeatureTable.from_gff3(geneset_agamp42_fn, attributes=attributes)


def load_geneset_agamp44(attributes=None):
    """Function to load data from GFF into a structured array. Can take a few seconds so put this
    into a function so user can decide whether to execute."""
    global geneset_agamp44
    geneset_agamp44 = allel.FeatureTable.from_gff3(geneset_agamp44_fn, attributes=attributes)


def get_geneset_features(geneset_fn, chrom, start=None, stop=None):
    """Function to load geneset features for a specific genome region via petl."""
    if start and stop:
        region = '%s:%s-%s' % (chrom, start, stop)
    else:
        region = chrom
    return etl.fromgff3(geneset_fn, region=region)


gene_labels = {
    'AGAP009195': 'Gste1',
    'AGAP009194': 'Gste2',
    'AGAP009197': 'Gste3',
    'AGAP009193': 'Gste4',
    'AGAP009192': 'Gste5',
    'AGAP009191': 'Gste6',
    'AGAP009196': 'Gste7',
    'AGAP009190': 'Gste8',
    'AGAP004707': 'Vgsc',
    'AGAP002862': 'Cyp6aa1',
    'AGAP013128': 'Cyp6aa2',
    'AGAP002863': 'Coeae6o',
    'AGAP002865': 'Cyp6p3',
    'AGAP002866': 'Cyp6p5',
    'AGAP002867': 'Cyp6p4',
    'AGAP002868': 'Cyp6p1',
    'AGAP002869': 'Cyp6p2',
    'AGAP002870': 'Cyp6ad1',
    'AGAP002915': 'Pcsk4/furin',
    'AGAP002825': 'Pp01',
    'AGAP002824': 'Gprtak1',
    'AGAP006028': 'Gaba',
    'AGAP010815': 'Tep1'
}


def plot_genes(genome, geneset_fn, chrom, start=1, stop=None, ax=None, height=.3, label=False, labels=None,
               label_unnamed=True, barh_kwargs=None):

    import matplotlib.pyplot as plt

    if stop is None:
        stop = len(genome[chrom])

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 1))
        sns.despine(ax=ax, offset=5)

    genes = get_geneset_features(geneset_fn, chrom, start, stop).eq('type', 'gene').records()

    fwd_ranges = [(g.start, (g.end - g.start)) for g in genes if g.strand == '+']
    rev_ranges = [(g.start, (g.end - g.start)) for g in genes if g.strand == '-']
    if barh_kwargs is None:
        barh_kwargs = dict()
    barh_kwargs.setdefault('color', 'k')
    ax.broken_barh(fwd_ranges, (.5, height), **barh_kwargs)
    ax.broken_barh(rev_ranges, (.5-height, height), **barh_kwargs)
    ax.set_ylim(0, 1)
    ax.axhline(.5, color='k', linestyle='-')
    ax.set_xlim(start, stop)
    ax.set_yticks([.5-(height/2), .5+(height/2)])
    ax.set_yticklabels(['-', '+'])
    ax.set_ylabel('genes', rotation=0, ha='right', va='center')

    if label:
        for gene in genes:
            gid = gene.attributes['ID']
            if labels and gid not in labels and not label_unnamed:
                continue
            if labels and gid in labels:
                label = labels[gid]
            else:
                label = gid
            x = gene.start
            if x < start:
                x = start
            if x > stop:
                x = stop
            if gene.strand == '+':
                rotation = 45
                y = .5 + height
                ax.text(x, y, label, rotation=rotation, fontsize=6, ha='left', va='bottom')
            else:
                rotation = -45
                y = .5 - height
                ax.text(x, y, label, rotation=rotation, fontsize=6, ha='left', va='top')


# variant callsets
##################

variation_dir = os.path.join(release_dir, 'variation')

# main callset
callset_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'all', 'ag1000g.phase2.ar1.h5')
callset_lite_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'lite', 'ag1000g.phase2.ar1.lite.h5')
callset_zarr_fn = os.path.join(variation_dir, 'main', 'zarr2', 'ag1000g.phase2.ar1')

# preference: zarr > hdf5 > hdf5 (lite)
if os.path.exists(callset_zarr_fn):
    callset = zarr.open_group(callset_zarr_fn, mode='r')
elif os.path.exists(callset_h5_fn):
    callset = h5py.File(callset_h5_fn, mode='r')
elif os.path.exists(callset_lite_h5_fn):
    callset = h5py.File(callset_lite_h5_fn, mode='r')

# main callset, PASS variants only
callset_pass_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'pass', 'ag1000g.phase2.ar1.pass.h5')
callset_pass_lite_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'lite', 'ag1000g.phase2.ar1.pass.lite.h5')
callset_pass_zarr_fn = os.path.join(variation_dir, 'main', 'zarr2', 'ag1000g.phase2.ar1.pass')

# preference: zarr > hdf5 > hdf5 (lite)
if os.path.exists(callset_pass_zarr_fn):
    callset_pass = zarr.open_group(callset_pass_zarr_fn, mode='r')
elif os.path.exists(callset_pass_h5_fn):
    callset_pass = h5py.File(callset_pass_h5_fn, mode='r')
elif os.path.exists(callset_pass_lite_h5_fn):
    callset_pass = h5py.File(callset_pass_lite_h5_fn, mode='r')

# main callset, PASS biallelic variants only
callset_pass_biallelic_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'biallelic', 'ag1000g.phase2.ar1.pass.biallelic.h5')
callset_pass_biallelic_lite_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'lite', 'ag1000g.phase2.ar1.pass.biallelic.lite.h5')
callset_pass_biallelic_zarr_fn = os.path.join(variation_dir, 'main', 'zarr2', 'ag1000g.phase2.ar1.pass.biallelic')

# preference: zarr > hdf5 > hdf5 (lite)
if os.path.exists(callset_pass_biallelic_zarr_fn):
    callset_pass_biallelic = zarr.open_group(callset_pass_biallelic_zarr_fn, mode='r')
elif os.path.exists(callset_pass_biallelic_h5_fn):
    callset_pass_biallelic = h5py.File(callset_pass_biallelic_h5_fn, mode='r')
elif os.path.exists(callset_pass_biallelic_lite_h5_fn):
    callset_pass_biallelic = h5py.File(callset_pass_biallelic_lite_h5_fn, mode='r')


# accessibility
###############

accessibility_dir = os.path.join(release_dir, 'accessibility')
accessibility_fn = os.path.join(accessibility_dir, 'accessibility.h5')
if os.path.exists(accessibility_fn):
    accessibility = h5py.File(accessibility_fn, mode='r')


# sample metadata
#################

samples_dir = os.path.join(release_dir, 'samples')
samples_fn = os.path.join(samples_dir, 'samples.meta.txt')
if os.path.exists(samples_fn):
    tbl_samples = (
        etl
        .fromtsv(samples_fn)
        .convert(('year', 'n_sequences'), int)
        .convert(('mean_coverage',), float)
    )
    lkp_samples = tbl_samples.recordlookupone('ox_code')
    sample_ids = tbl_samples.values('ox_code').list()
    samples = pandas.read_csv(samples_fn, sep='\t', index_col='ox_code')


# populations
#############

pop_ids = (
    'AOcol',
    'BFcol',
    'GHcol',
    'CIcol',
    'GNcol',
    'GW',
    'GM',
    'GNgam',
    'BFgam',
    'GHgam',
    'CMgam',
    'UGgam',
    'GAgam',
    'GQgam',
    'FRgam',
    'KE',
)

pop_labels = {
    'AOcol': 'Angola $coluzzii$',
    'BFcol': 'Burkina Faso $coluzzii$',
    'GHcol': 'Ghana $coluzzii$',
    'CIcol': "Côte d'Ivoire $coluzzii$",
    'GNcol': 'Guinea $coluzzii$',
    'GW': 'Guinea-Bissau',
    'GM': 'The Gambia',
    'GNgam': 'Guinea $gambiae$',
    'BFgam': 'Burkina Faso $gambiae$',
    'GHgam': 'Ghana $gambiae$',
    'CMgam': 'Cameroon $gambiae$',
    'UGgam': 'Uganda $gambiae$',
    'GAgam': 'Gabon $gambiae$',
    'GQgam': 'Bioko $gambiae$',
    'FRgam': 'Mayotte $gambiae$',
    'KE': 'Kenya',
    'colony': 'colony',
}

# TODO pop_colors


# extras
########

extras_dir = os.path.join(release_dir, 'extras')

# allele counts
allele_counts_fn = os.path.join(extras_dir, 'allele_counts.h5')
if os.path.exists(allele_counts_fn):
    allele_counts = h5py.File(allele_counts_fn, mode='r')
