# -*- coding: utf-8 -*-
"""
This module contains convenience variables relating to the Ag1000G phase 1 AR3 data release.

Use this module in notebooks and scripts as follows:

    >>> import sys
    >>> sys.path.insert(0, '/path/to/malariagen/ag1000g/src/python')
    >>> from ag1k import phase1_ar3

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


# fundamentals
##############

title = 'Phase 1 AR3 release'
release_dir = '/kwiat/vector/ag1000g/release/phase1.AR3'


# reference sequence
####################

chromosomes = '2R', '2L', '3R', '3L', 'X', 'Y_unplaced', 'UNKN'
autosomes = chromosomes[:4]
genome_dir = os.path.join(release_dir, 'genome')
genome_fn = os.path.join(genome_dir, 'Anopheles-gambiae-PEST_CHROMOSOMES_AgamP3.fa')
if os.path.exists(genome_fn):
    genome = pyfasta.Fasta(genome_fn)


# genome annotations
####################

geneset_dir = os.path.join(release_dir, 'geneset')
geneset_fn = os.path.join(geneset_dir, 'Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.2.sorted.gff3.gz')


def load_geneset():
    """Function to load data from GFF into a structured array. Can take a few seconds so put this
    into a function so user can decide whether to execute."""
    global geneset
    if os.path.exists(geneset_fn):
        geneset = allel.FeatureTable.from_gff3(geneset_fn)


def get_geneset_features(chrom, start=None, stop=None):
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


def plot_genes(chrom, start=1, stop=None, ax=None, height=.3, label=False, labels=None,
               label_unnamed=True, barh_kwargs=None):

    import matplotlib.pyplot as plt

    if stop is None:
        stop = len(genome[chrom])

    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 1))
        sns.despine(ax=ax, offset=5)

    genes = get_geneset_features(chrom, start, stop).eq('type', 'gene').records()

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
callset_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'ag1000g.phase1.ar3.h5')
if os.path.exists(callset_h5_fn):
    callset = h5py.File(callset_h5_fn, mode='r')

# main callset, PASS variants only
callset_pass_h5_fn = os.path.join(variation_dir, 'main', 'hdf5', 'ag1000g.phase1.ar3.pass.h5')
if os.path.exists(callset_pass_h5_fn):
    callset_pass = h5py.File(callset_pass_h5_fn, mode='r')


# accessibility
###############

accessibility_dir = os.path.join(release_dir, 'accessibility')
accessibility_fn = os.path.join(accessibility_dir, 'accessibility.h5')
if os.path.exists(accessibility_fn):
    accessibility = h5py.File(accessibility_fn, mode='r')


# sample metadata
#################

samples_dir = os.path.join(release_dir, 'samples')
samples_fn = os.path.join(samples_dir, 'samples.all.txt')
if os.path.exists(samples_fn):
    tbl_samples = (
        etl
        .fromtsv(samples_fn)
        .convert(('index', 'year', 'n_sequences', 'kt_2la', 'kt_2rb'), int)
        .convert(('mean_coverage', 'latitude', 'longitude') + tuple(range(20, 36)), float)
    )
    lkp_samples = tbl_samples.recordlookupone('ox_code')
    sample_ids = tbl_samples.values('ox_code').list()
    samples = pandas.read_csv(samples_fn, sep='\t', index_col='index')


# populations
#############

pop_ids = 'AOM', 'BFM', 'GWA', 'GNS', 'BFS', 'CMS', 'GAS', 'UGS', 'KES'

pop_labels = {
    'AOM': 'AO $coluzzii$',
    'BFM': 'BF $coluzzii$',
    'GWA': 'GW',
    'GNS': 'GN $gambiae$',
    'BFS': 'BF $gambiae$',
    'CMS': 'CM $gambiae$',
    'UGS': 'UG $gambiae$',
    'GAS': 'GA $gambiae$',
    'KES': 'KE',
    'colony': 'colony',
}

pop_colors = {
    'AOM': sns.color_palette('YlOrBr', 5)[4],
    'BFM': sns.color_palette('Reds', 3)[1],
    'GWA': sns.color_palette('YlOrBr', 5)[1],
    'GNS': sns.color_palette('Blues', 3)[0],
    'BFS': sns.color_palette('Blues', 3)[1],
    'CMS': sns.color_palette('Blues', 3)[2],
    'UGS': sns.color_palette('Greens', 2)[0],
    'GAS': sns.color_palette('Greens', 2)[1],
    'KES': sns.color_palette('Greys', 5)[2],
    'colony': sns.color_palette('Greys', 5)[-1]
}
# convert to hex notation for ease of use elsewhere
for p in pop_colors:
    h = '#%02x%02x%02x' % tuple(int(255*c) for c in pop_colors[p])


# extras
########

extras_dir = os.path.join(release_dir, 'extras')

# allele counts
allele_counts_fn = os.path.join(extras_dir, 'allele_counts.h5')
if os.path.exists(allele_counts_fn):
    allele_counts = h5py.File(allele_counts_fn, mode='r')
allele_counts_gq10_fn = os.path.join(extras_dir, 'allele_counts.gq10.h5')
if os.path.exists(allele_counts_gq10_fn):
    allele_counts_gq10 = h5py.File(allele_counts_gq10_fn, mode='r')

# outgroup data
outgroup_species = 'arab', 'meru', 'mela', 'quad', 'epir', 'chri'
outgroup_alleles_fn = os.path.join(extras_dir, 'outgroup_alleles.h5')
if os.path.exists(outgroup_alleles_fn):
    outgroup_alleles = h5py.File(outgroup_alleles_fn, mode='r')
outgroup_allele_counts_fn = os.path.join(extras_dir, 'outgroup_allele_counts.h5')
if os.path.exists(outgroup_allele_counts_fn):
    outgroup_allele_counts = h5py.File(outgroup_allele_counts_fn, mode='r')


# misc
######

# chromatin
_data_chromatin = b"""CHX     chro    X       20009764        24393108
CH2R    chro    2R      58984778        61545105
CH2L    chro    2L      1       2431617
PEU2L   chro    2L      2487770 5042389
IH2L    chro    2L      5078962 5788875
IH3R    chro    3R      38988757        41860198
CH3R    chro    3R      52161877        53200684
CH3L    chro    3L      1       1815119
PEU3L   chro    3L      1896830 4235209
IH3L    chro    3L      4264713 5031692
"""
tbl_chromatin = (
    etl
    .fromtext(etl.MemorySource(_data_chromatin))
    .split('lines', '\s+', ['name', 'type', 'chrom', 'start', 'stop'])
    .convert(('start', 'stop'), int)
    .cutout('type')
)

# genome regions
region_X_speciation = 'X-speciation', 'X', 15000000, 24000000
region_X_free = 'X-free', 'X', 1, 14000000
region_3L_free = '3L-free', '3L', 15000000, 41000000
region_3R_free = '3R-free', '3R', 1, 37000000
