# -*- coding: utf-8 -*-
"""
General purpose utility functions.

"""
from __future__ import absolute_import, print_function, division


# standard library imports
import contextlib
import sys
import datetime


# third party library imports
import humanize


_slog_indent = -2


def log(*msg):
    """Simple logging function that flushes immediately to stdout."""
    s = ' '.join(map(str, msg))
    print(s, file=sys.stdout)
    sys.stdout.flush()


@contextlib.contextmanager
def timer(*msg):
    before = datetime.datetime.now()
    try:
        yield
    except:
        after = datetime.datetime.now()
        elapsed = (after - before).total_seconds()
        done = 'errored after %s' % humanize.naturaldelta(elapsed)
        if not msg:
            msg = done
        else:
            msg = ', '.join(map(str, msg)) + ', ' + done
        print(msg, file=sys.stderr)
        sys.stderr.flush()
        raise
    else:
        after = datetime.datetime.now()
        elapsed = (after - before).total_seconds()
        done = 'done in %s' % humanize.naturaldelta(elapsed)
        if not msg:
            msg = done
        else:
            msg = ', '.join(map(str, msg)) + ', ' + done
        print(msg, file=sys.stdout)
        sys.stdout.flush()


@contextlib.contextmanager
def section(*title):
    global _slog_indent
    before = datetime.datetime.now()
    _slog_indent += 2
    prefix = (' ' * _slog_indent) + '[' + ', '.join(map(str, title)) + '] '

    def slog(*msg, file=sys.stdout):
        print(prefix + ' '.join(map(str, msg)), file=file)
        file.flush()

    slog('begin')

    try:
        yield slog

    except:
        after = datetime.datetime.now()
        elapsed = (after - before).total_seconds()
        msg = 'errored after %s' % humanize.naturaldelta(elapsed)
        slog(msg, file=sys.stderr)
        _slog_indent -= 2
        raise

    else:
        after = datetime.datetime.now()
        elapsed = (after - before).total_seconds()
        msg = 'done in %s' % humanize.naturaldelta(elapsed)
        slog(msg, file=sys.stdout)
        _slog_indent -= 2


def _h5ls(h5o, currentdepth, maxdepth, maxitems, prefix):
    if maxdepth is not None and currentdepth == maxdepth:
        return
    for i, k in enumerate(h5o.keys()):
        path = prefix + '/' + k
        if maxitems is not None and i == maxitems:
            print(prefix + '/...')
            break
        v = h5o[k]
        print(path + ' : ' + repr(v))
        if hasattr(v, 'keys'):
            _h5ls(v, currentdepth+1, maxdepth=maxdepth, maxitems=maxitems, prefix=path)


def h5ls(h5o, maxdepth=None, maxitems=None):
    """Obtain a recursive listing of the contents of an HDF5 file or group."""
    _h5ls(h5o, 0, maxdepth=maxdepth, maxitems=maxitems, prefix='')


def fig_linear_genome(plotf, genome, chromosomes=('2R', '2L', '3R', '3L', 'X'),
                      fig=None, bottom=0, height=1, width_factor=1.08, chrom_pad=0.035,
                      clip_patch_kwargs=None, **kwargs):
    """Utility function to make a linear genome figure.

    Parameters
    ----------
    plotf : function
        Function to plot a single chromosome. Must accept 'chrom' and 'ax' arguments and also
        flexible **kwargs.
    genome : pyfasta.Fasta
        Reference sequence. Used to compute genome and chromosome sizes.
    chromosomes : tuple of strings, optional
        Chromosomes to plot.
    fig : figure, optional
        Figure to plot on. If not provided, a new figure will be created.
    bottom : float, optional
        Figure coordinate to position bottom of axes.
    height : float, optional
        Figure height to use for axes.
    width_factor : float, optional
        Used to scale width of each chromosome subplot.
    chrom_pad : float, optional
        Used to set padding between chromosomes.
    clip_patch_kwargs : dict-like, optional
        Arguments for the clip path if used.
    **kwargs
        Passed through to `plotf`.

    Returns
    -------
    axs : dict
        A dictionary mapping chromosome names onto axes objects.

    """

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from matplotlib.path import Path

    # compute assembled genome size
    genome_size = sum(len(genome[chrom]) for chrom in chromosomes)

    # setup figure
    if fig is None:
        fig = plt.figure(figsize=(8, 1))

    # setup clip patch
    if clip_patch_kwargs is None:
        clip_patch_kwargs = dict()
    clip_patch_kwargs.setdefault('edgecolor', 'k')
    clip_patch_kwargs.setdefault('facecolor', 'none')
    clip_patch_kwargs.setdefault('lw', 1)

    # setup axes
    left = 0
    axs = dict()

    for chrom in chromosomes:

        # calculate width needed for this chrom
        width = len(genome[chrom]) / (genome_size * width_factor)

        # create axes
        ax = fig.add_axes([left, bottom, width, height])
        ax.set_axis_bgcolor((1, 1, 1, 0))
        axs[chrom] = ax

        # construct clip path
        if chrom in {'2R', '3R'}:
            verts = [(0.01, 0.02), (0.9, 0.02), (1.01, 0.3), (1.01, 0.7), (0.9, .98), (0.01, .98), (0.01, 0.02)]
            codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        elif chrom == "X":
            verts = [(0.01, 0.02), (0.9, 0.02), (0.99, 0.3), (0.99, 0.7), (0.9, .98), (0.01, .98), (0.01, 0.02)]
            codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        else:
            verts = [(0.1, 0.02), (.99, 0.02), (.99, .98), (.1, .98), (-0.01, .7), (-0.01, .3), (0.1, 0.02)]
            codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
        path = Path(verts, codes)
        clip_patch = mpl.patches.PathPatch(path, transform=ax.transAxes, **clip_patch_kwargs)

        # do the plotting
        plotf(chrom=chrom, ax=ax, clip_patch=clip_patch, **kwargs)

        # increment left coordinate
        left += len(genome[chrom]) / (genome_size * width_factor)
        if chrom in {'2L', '3L'}:
            left += chrom_pad

    return axs
