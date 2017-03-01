
# Extract mutations in VGSC

This notebook extracts data on all mutations in the VGSC gene.

## Setup


```python
%run setup.ipynb
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
# download gene annotations from vectorbase
!wget \
    --no-clobber \
    -O ../data/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.gff3.gz \
    https://www.vectorbase.org/download/anopheles-gambiae-pestbasefeaturesagamp44gff3gz

```

    File `../data/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.gff3.gz' already there; not retrieving.



```python
# download the Davies et al. (2007) gene models
!wget \
    --no-clobber \
    -O ../data/davies_vgsc_model_20170125.gff3 \
    http://alimanfoo.github.io/assets/davies_vgsc_model_20170125.gff3

```

    File `../data/davies_vgsc_model_20170125.gff3' already there; not retrieving.



```python
# load the vectorbase geneset
geneset_agamp44 = allel.FeatureTable.from_gff3('../data/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.gff3.gz',
                                               attributes=['ID', 'Parent'])
geneset_agamp44 = geneset_to_pandas(geneset_agamp44)
geneset_agamp44.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>seqid</th>
      <th>source</th>
      <th>type</th>
      <th>start</th>
      <th>end</th>
      <th>score</th>
      <th>strand</th>
      <th>phase</th>
      <th>ID</th>
      <th>Parent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>chromosome</td>
      <td>1</td>
      <td>49364325</td>
      <td>-1</td>
      <td>.</td>
      <td>-1</td>
      <td>2L</td>
      <td>.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>gene</td>
      <td>157348</td>
      <td>186936</td>
      <td>-1</td>
      <td>-</td>
      <td>-1</td>
      <td>AGAP004677</td>
      <td>.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>mRNA</td>
      <td>157348</td>
      <td>181305</td>
      <td>-1</td>
      <td>-</td>
      <td>-1</td>
      <td>AGAP004677-RA</td>
      <td>AGAP004677</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>three_prime_UTR</td>
      <td>157348</td>
      <td>157495</td>
      <td>-1</td>
      <td>-</td>
      <td>-1</td>
      <td>.</td>
      <td>AGAP004677-RA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>exon</td>
      <td>157348</td>
      <td>157623</td>
      <td>-1</td>
      <td>-</td>
      <td>-1</td>
      <td>.</td>
      <td>AGAP004677-RA</td>
    </tr>
  </tbody>
</table>
</div>




```python
# subset to VGSC
region_vgsc = SeqFeature('2L', 2358158, 2431617)
geneset_agamp44_vgsc = geneset_agamp44.query(region_vgsc.query).copy()
# replace CDS IDs as not informative
geneset_agamp44_vgsc['ID'].values[(geneset_agamp44_vgsc.type == 'CDS').values] = ''
geneset_agamp44_vgsc.type.value_counts()
```




    CDS     93
    exon    93
    mRNA     3
    gene     1
    Name: type, dtype: int64




```python
# load the Davies geneset
geneset_davies = allel.FeatureTable.from_gff3('../data/davies_vgsc_model_20170125.gff3',
                                              attributes=['ID', 'Parent'])
geneset_davies = geneset_to_pandas(geneset_davies)
geneset_davies.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>seqid</th>
      <th>source</th>
      <th>type</th>
      <th>start</th>
      <th>end</th>
      <th>score</th>
      <th>strand</th>
      <th>phase</th>
      <th>ID</th>
      <th>Parent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C1N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C3N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C5N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C7N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C8N2</td>
      <td>AGAP004707</td>
    </tr>
  </tbody>
</table>
</div>




```python
# make a combined geneset
geneset_vgsc_combined = pandas.concat([geneset_agamp44_vgsc, geneset_davies])
geneset_vgsc_combined.query("type == 'mRNA'")
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>seqid</th>
      <th>source</th>
      <th>type</th>
      <th>start</th>
      <th>end</th>
      <th>score</th>
      <th>strand</th>
      <th>phase</th>
      <th>ID</th>
      <th>Parent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>666</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>AGAP004707-RA</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>729</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>AGAP004707-RB</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>792</th>
      <td>2L</td>
      <td>VectorBase</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>AGAP004707-RC</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C1N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C3N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C5N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C7N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C8N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C10N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C11N2</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C1N9</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C8N9</td>
      <td>AGAP004707</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2L</td>
      <td>Davies et al. (2007)</td>
      <td>mRNA</td>
      <td>2358158</td>
      <td>2431617</td>
      <td>-1</td>
      <td>+</td>
      <td>-1</td>
      <td>Davies-C1N9ck</td>
      <td>AGAP004707</td>
    </tr>
  </tbody>
</table>
</div>




```python
# setup a variant annotator
annotator = veff.Annotator(
    fasta_path='../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3/genome/Anopheles-gambiae-PEST_CHROMOSOMES_AgamP3.fa', 
    gff3_path=['../data/Anopheles-gambiae-PEST_BASEFEATURES_AgamP4.4.gff3.gz',
               '../data/davies_vgsc_model_20170125.gff3'],
    seqid='2L'
)
```


```python
# identify VGSC transcripts
transcript_ids = [f.feature_id for f in annotator.get_children('AGAP004707')]
transcript_ids
```




    ['AGAP004707-RA',
     'AGAP004707-RB',
     'AGAP004707-RC',
     'Davies-C1N2',
     'Davies-C3N2',
     'Davies-C5N2',
     'Davies-C7N2',
     'Davies-C8N2',
     'Davies-C10N2',
     'Davies-C11N2',
     'Davies-C1N9',
     'Davies-C8N9',
     'Davies-C1N9ck']




```python
# tabulate Davies exons
tbl_davies_exons = (
    etl
    .fromdataframe(geneset_davies)
    .eq('type', 'CDS')
    .cutout('Parent', 'source', 'type', 'score', 'strand', 'phase')
    .merge(key=('start', 'end'))
    .rename('seqid', 'exon_seqid')
    .rename('ID', 'exon')
    .rename('start', 'exon_start')
    .rename('end', 'exon_end')
    .movefield('exon_seqid', 0)
)
tbl_davies_exons.displayall()
```


<table class='petl'>
<thead>
<tr>
<th>0|exon_seqid</th>
<th>1|exon_start</th>
<th>2|exon_end</th>
<th>3|exon</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td style='text-align: right'>2358158</td>
<td style='text-align: right'>2358304</td>
<td>1</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2359640</td>
<td style='text-align: right'>2359672</td>
<td>2j</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2381065</td>
<td style='text-align: right'>2381270</td>
<td>4</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2382270</td>
<td style='text-align: right'>2382398</td>
<td>5</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2385694</td>
<td style='text-align: right'>2385785</td>
<td>6</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2390129</td>
<td style='text-align: right'>2390341</td>
<td>7</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2390425</td>
<td style='text-align: right'>2390485</td>
<td>8</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2390594</td>
<td style='text-align: right'>2390738</td>
<td>9</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2391156</td>
<td style='text-align: right'>2391320</td>
<td>10</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2399898</td>
<td style='text-align: right'>2400173</td>
<td>11i+</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2401549</td>
<td style='text-align: right'>2401569</td>
<td>12</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2402447</td>
<td style='text-align: right'>2402509</td>
<td>13a</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2403086</td>
<td style='text-align: right'>2403269</td>
<td>14</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2407622</td>
<td style='text-align: right'>2407818</td>
<td>15</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2407894</td>
<td style='text-align: right'>2407993</td>
<td>16</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2408071</td>
<td style='text-align: right'>2408139</td>
<td>17</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2416794</td>
<td style='text-align: right'>2417071</td>
<td>18b+</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2417185</td>
<td style='text-align: right'>2417358</td>
<td>19</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2417637</td>
<td style='text-align: right'>2417799</td>
<td>20c</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2421385</td>
<td style='text-align: right'>2421547</td>
<td>20d</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2422468</td>
<td style='text-align: right'>2422655</td>
<td>21</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2422713</td>
<td style='text-align: right'>2422920</td>
<td>22</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2424207</td>
<td style='text-align: right'>2424418</td>
<td>23f+</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2424237</td>
<td style='text-align: right'>2424418</td>
<td>23f-</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2424651</td>
<td style='text-align: right'>2424870</td>
<td>24h+</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2424729</td>
<td style='text-align: right'>2424870</td>
<td>24h-</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2424946</td>
<td style='text-align: right'>2425211</td>
<td>25</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2425278</td>
<td style='text-align: right'>2425451</td>
<td>26</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2425770</td>
<td style='text-align: right'>2425892</td>
<td>27k</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2427988</td>
<td style='text-align: right'>2428110</td>
<td>27l</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2429097</td>
<td style='text-align: right'>2429219</td>
<td>28</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2429282</td>
<td style='text-align: right'>2429476</td>
<td>29</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2429556</td>
<td style='text-align: right'>2429801</td>
<td>30</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2429872</td>
<td style='text-align: right'>2430142</td>
<td>31</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2430224</td>
<td style='text-align: right'>2430528</td>
<td>32</td>
</tr>
<tr>
<td>2L</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
</tr>
</tbody>
</table>



## Extract table of variants


```python
callset = zarr.open_group('../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3.1/variation/main/zarr2/ag1000g.phase1.ar3', mode='r')
callset
```




    Group(/, 8)
      arrays: 1; samples
      groups: 7; 2L, 2R, 3L, 3R, UNKN, X, Y_unplaced
      store: DirectoryStore




```python
# what fields are available?
print(', '.join(callset['2L/variants']))
```

    ABHet, ABHom, AC, AF, ALT, AN, ANN, Accessible, BaseCounts, BaseQRankSum, CHROM, Coverage, CoverageMQ0, DP, DS, Dels, FILTER_FS, FILTER_HRun, FILTER_HighCoverage, FILTER_HighMQ0, FILTER_LowCoverage, FILTER_LowMQ, FILTER_LowQual, FILTER_NoCoverage, FILTER_PASS, FILTER_QD, FILTER_ReadPosRankSum, FILTER_RefN, FILTER_RepeatDUST, FS, HRun, HW, HaplotypeScore, HighCoverage, HighMQ0, InbreedingCoeff, LOF, LowCoverage, LowMQ, LowPairing, MLEAC, MLEAF, MQ, MQ0, MQRankSum, NDA, NMD, NoCoverage, OND, POS, QD, QUAL, REF, RPA, RU, ReadPosRankSum, RefMasked, RefN, RepeatDUST, RepeatMasker, RepeatTRF, STR, VariantType, is_snp, num_alleles, svlen



```python
# what SNPEFF fields are available?
print(', '.join(callset['2L/variants/ANN'].dtype.names))
```

    Allele, Annotation, Annotation_Impact, Gene_Name, Gene_ID, Feature_Type, Feature_ID, Transcript_BioType, Rank, HGVS_c, HGVS_p, cDNA_pos, cDNA_length, CDS_pos, CDS_length, AA_pos, AA_length, Distance



```python
samples = pandas.read_csv('../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3/samples/samples.meta.txt',
                          sep='\t', index_col='index')
samples.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ox_code</th>
      <th>src_code</th>
      <th>sra_sample_accession</th>
      <th>population</th>
      <th>country</th>
      <th>region</th>
      <th>contributor</th>
      <th>contact</th>
      <th>year</th>
      <th>m_s</th>
      <th>sex</th>
      <th>n_sequences</th>
      <th>mean_coverage</th>
      <th>latitude</th>
      <th>longitude</th>
    </tr>
    <tr>
      <th>index</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AB0085-C</td>
      <td>BF2-4</td>
      <td>ERS223996</td>
      <td>BFS</td>
      <td>Burkina Faso</td>
      <td>Pala</td>
      <td>Austin Burt</td>
      <td>Sam O'Loughlin</td>
      <td>2012</td>
      <td>S</td>
      <td>F</td>
      <td>89905852</td>
      <td>28.01</td>
      <td>11.150</td>
      <td>-4.235</td>
    </tr>
    <tr>
      <th>1</th>
      <td>AB0087-C</td>
      <td>BF3-3</td>
      <td>ERS224013</td>
      <td>BFM</td>
      <td>Burkina Faso</td>
      <td>Bana</td>
      <td>Austin Burt</td>
      <td>Sam O'Loughlin</td>
      <td>2012</td>
      <td>M</td>
      <td>F</td>
      <td>116706234</td>
      <td>36.76</td>
      <td>11.233</td>
      <td>-4.472</td>
    </tr>
    <tr>
      <th>2</th>
      <td>AB0088-C</td>
      <td>BF3-5</td>
      <td>ERS223991</td>
      <td>BFM</td>
      <td>Burkina Faso</td>
      <td>Bana</td>
      <td>Austin Burt</td>
      <td>Sam O'Loughlin</td>
      <td>2012</td>
      <td>M</td>
      <td>F</td>
      <td>112090460</td>
      <td>23.30</td>
      <td>11.233</td>
      <td>-4.472</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AB0089-C</td>
      <td>BF3-8</td>
      <td>ERS224031</td>
      <td>BFM</td>
      <td>Burkina Faso</td>
      <td>Bana</td>
      <td>Austin Burt</td>
      <td>Sam O'Loughlin</td>
      <td>2012</td>
      <td>M</td>
      <td>F</td>
      <td>145350454</td>
      <td>41.36</td>
      <td>11.233</td>
      <td>-4.472</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AB0090-C</td>
      <td>BF3-10</td>
      <td>ERS223936</td>
      <td>BFM</td>
      <td>Burkina Faso</td>
      <td>Bana</td>
      <td>Austin Burt</td>
      <td>Sam O'Loughlin</td>
      <td>2012</td>
      <td>M</td>
      <td>F</td>
      <td>105012254</td>
      <td>34.64</td>
      <td>11.233</td>
      <td>-4.472</td>
    </tr>
  </tbody>
</table>
</div>




```python
def tabulate_variants(callset, snpeff, seqid, start, end, pop_ids, subpops):
    """Build a table of variants for a given callset and genome region."""
    
    variants = callset[seqid]['variants']
    ann = snpeff[seqid]['variants']['ANN']
    pos = allel.SortedIndex(variants['POS'])
    loc = pos.locate_range(start, end)
    genotype = allel.GenotypeArray(callset[seqid]['calldata/genotype'][loc])
    acs = genotype.count_alleles_subpops(max_allele=3, subpops=subpops)
    
    # extract columns
    variants_fields = [
        'CHROM',
        'POS',
        'num_alleles',
        'REF',
        'ALT',
        'AC',
        'FILTER_PASS',
        'NoCoverage',
        'LowCoverage',
        'HighCoverage',
        'LowMQ',
        'HighMQ0',
        'RepeatDUST',
        'RepeatMasker',
        'RepeatTRF',
        'FS',
        'HRun',
        'QD',
        'ReadPosRankSum',
    ]
    ann_fields = ['Allele', 'Annotation', 'HGVS_c', 'HGVS_p', 'Feature_ID']
    cols = (
        [variants[f][loc] for f in variants_fields] + 
        [ann[loc][f] for f in ann_fields] + 
        [acs[p].to_frequencies() for p in pop_ids]
    )

    def split_alleles(row):
        for i in range(row.num_alleles - 1):
            # break down alleles
            out = [
                row['CHROM'], 
                row['POS'], 
                row['num_alleles'], 
                row['REF'], 
                row['ALT'][i], 
                row['AC'][i], 
                i, 
            ]
            # add in remaining variant annotations
            out += [row[f] for f in variants_fields[6:]]
            # SNPEFF annotation only applies to first allele
            if i == 0:
                out += [row[f] for f in ann_fields]
            else:
                out += [None for f in ann_fields]
            # add in population allele frequencies
            out += [row[p][i+1] for p in pop_ids]
            yield out
        
    tbl = (
        etl
        .fromcolumns(cols, header=variants_fields + ann_fields + list(pop_ids))
        .rowmapmany(split_alleles, header=variants_fields[:6] + ['ALTIX'] + variants_fields[6:] + ann_fields + list(pop_ids), failonerror=True)
        .convert('CHROM REF ALT Allele Annotation HGVS_c HGVS_p Feature_ID'.split(), lambda v: str(v, 'ascii'))
        .rename({f: 'SNPEFF_' + f for f in ann_fields})
        .rename({p: 'AF_%s' % p for p in pop_ids})
        .addfield('check_allele', lambda row: row['SNPEFF_Allele'] is None or row['SNPEFF_Allele'] == row['ALT'])
    )
    
    return tbl
```


```python
pop_ids = 'AOM BFM GWA GNS BFS CMS GAS UGS KES'.split()
```


```python
subpops = {p: samples[samples.population == p].index.values.tolist() for p in pop_ids}
```


```python
# build a table of variants from phase 1
tbl_variants_phase1 = tabulate_variants(callset, callset, 
                                        seqid=region_vgsc.seqid, start=region_vgsc.start, end=region_vgsc.end, 
                                        pop_ids=pop_ids, subpops=subpops)
tbl_variants_phase1
```




<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
</tr>
<tr>
<td>2L</td>
<td>2358316</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>73</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4844</td>
<td>0</td>
<td>16.438</td>
<td>1.4219</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+12T>G</td>
<td>.</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.132727272727</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
</tr>
<tr>
<td>2L</td>
<td>2358328</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.7363</td>
<td>0</td>
<td>16.062</td>
<td>-0.646</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+24T>C</td>
<td>.</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
</tr>
<tr>
<td>2L</td>
<td>2358353</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9512</td>
<td>0</td>
<td>9.8594</td>
<td>1.1582</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+49C>T</td>
<td>.</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
</tr>
<tr>
<td>2L</td>
<td>2358405</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>6</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.844</td>
<td>1</td>
<td>10.859</td>
<td>1.1562</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+101T>A</td>
<td>.</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>



## Annotate effects for all transcripts


```python
cds_effects = [
    'NON_SYNONYMOUS_CODING', 
    'SYNONYMOUS_CODING',    
]
intron_effects = [
    'INTRONIC', 
    'SPLICE_CORE',
    'SPLICE_REGION',        
]
selected_effects = cds_effects + intron_effects
```


```python
def lpop(l, default=None):
    """Pop the first item from a list if not empty."""
    try:
        return l[0]
    except IndexError:
        return default

```


```python
def transcript_effect(transcript_id):
    def f(row):
        e = lpop([e for e in row.VEFF if e.transcript_id == transcript_id])
        if e and e.effect in cds_effects:
            return (e.effect, e.aa_change)
        elif e and e.effect in intron_effects:
            return (e.effect, e.intron_cds_5prime, e.intron_5prime_dist, e.intron_cds_3prime, e.intron_3prime_dist)
        else:
            return None
    return f

```


```python
tbl_variants_phase1_eff = (
    tbl_variants_phase1
    # join in Davies exon information
    .intervalleftjoin(
        # don't include shorter exon alternatives
        tbl_davies_exons.select('exon', lambda v: v[-1] != '-'),
        lkey='CHROM', rkey='exon_seqid', lstart='POS', rstart='exon_start', lstop='POS', rstop='exon_end', include_stop=True)
    .cutout('exon_seqid')
    .addfield('VEFF', lambda row: [e for e in annotator.get_effects(chrom=row.CHROM, pos=row.POS, ref=row.REF, alt=row.ALT) 
                                   if e.effect in selected_effects])
    .addfield(transcript_ids[0], transcript_effect(transcript_ids[0]))
    .addfield(transcript_ids[1], transcript_effect(transcript_ids[1]))
    .addfield(transcript_ids[2], transcript_effect(transcript_ids[2]))
    .addfield(transcript_ids[3], transcript_effect(transcript_ids[3]))
    .addfield(transcript_ids[4], transcript_effect(transcript_ids[4]))
    .addfield(transcript_ids[5], transcript_effect(transcript_ids[5]))
    .addfield(transcript_ids[6], transcript_effect(transcript_ids[6]))
    .addfield(transcript_ids[7], transcript_effect(transcript_ids[7]))
    .addfield(transcript_ids[8], transcript_effect(transcript_ids[8]))
    .addfield(transcript_ids[9], transcript_effect(transcript_ids[9]))
    .addfield(transcript_ids[10], transcript_effect(transcript_ids[10]))
    .addfield(transcript_ids[11], transcript_effect(transcript_ids[11]))
    .addfield(transcript_ids[12], transcript_effect(transcript_ids[12]))
    .cutout('VEFF')
    .replaceall('.', None)
    .replaceall('', None)
    .cache()
)
```


```python
tbl_variants_phase1_eff.display(20)
```


<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2358158</td>
<td style='text-align: right'>2358304</td>
<td>1</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
</tr>
<tr>
<td>2L</td>
<td>2358316</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>73</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4844</td>
<td>0</td>
<td>16.438</td>
<td>1.4219</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+12T>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.132727272727</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 12, 'AGAP004707-PA', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PB', 12, 'AGAP004707-PB', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PC', 12, 'AGAP004707-PC', -3691)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
</tr>
<tr>
<td>2L</td>
<td>2358328</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.7363</td>
<td>0</td>
<td>16.062</td>
<td>-0.646</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+24T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 24, 'AGAP004707-PA', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PB', 24, 'AGAP004707-PB', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PC', 24, 'AGAP004707-PC', -3679)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
</tr>
<tr>
<td>2L</td>
<td>2358353</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9512</td>
<td>0</td>
<td>9.8594</td>
<td>1.1582</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+49C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 49, 'AGAP004707-PA', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PB', 49, 'AGAP004707-PB', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PC', 49, 'AGAP004707-PC', -3654)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
</tr>
<tr>
<td>2L</td>
<td>2358405</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>6</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.844</td>
<td>1</td>
<td>10.859</td>
<td>1.1562</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+101T>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 101, 'AGAP004707-PA', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PB', 101, 'AGAP004707-PB', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PC', 101, 'AGAP004707-PC', -3602)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
</tr>
<tr>
<td>2L</td>
<td>2358441</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>78</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>6</td>
<td>17</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4805</td>
<td>1</td>
<td>21.703</td>
<td>0.94385</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+137A>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0145454545455</td>
<td style='text-align: right'>0.625</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 137, 'AGAP004707-PA', -3566)</td>
<td>('INTRONIC', 'AGAP004707-PB', 137, 'AGAP004707-PB', -3566)</td>
<td>('INTRONIC', 'AGAP004707-PC', 137, 'AGAP004707-PC', -3566)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '2j', -1199)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
<td>('INTRONIC', '1', 137, '2j', -1199)</td>
<td>('INTRONIC', '1', 137, '3', -3548)</td>
</tr>
<tr>
<td>2L</td>
<td>2358463</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>5</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>4</td>
<td>16</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>22.0</td>
<td>0</td>
<td>15.211</td>
<td>-0.42798</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+159G>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0568181818182</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 159, 'AGAP004707-PA', -3544)</td>
<td>('INTRONIC', 'AGAP004707-PB', 159, 'AGAP004707-PB', -3544)</td>
<td>('INTRONIC', 'AGAP004707-PC', 159, 'AGAP004707-PC', -3544)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '2j', -1177)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
<td>('INTRONIC', '1', 159, '2j', -1177)</td>
<td>('INTRONIC', '1', 159, '3', -3526)</td>
</tr>
<tr>
<td>2L</td>
<td>2358468</td>
<td>2</td>
<td>A</td>
<td>C</td>
<td>150</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>4</td>
<td>17</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.668</td>
<td>0</td>
<td>19.812</td>
<td>-0.198</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+164A>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0978260869565</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0509090909091</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.52427184466</td>
<td style='text-align: right'>0.0568181818182</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 164, 'AGAP004707-PA', -3539)</td>
<td>('INTRONIC', 'AGAP004707-PB', 164, 'AGAP004707-PB', -3539)</td>
<td>('INTRONIC', 'AGAP004707-PC', 164, 'AGAP004707-PC', -3539)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '2j', -1172)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
<td>('INTRONIC', '1', 164, '2j', -1172)</td>
<td>('INTRONIC', '1', 164, '3', -3521)</td>
</tr>
<tr>
<td>2L</td>
<td>2358501</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>5</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>4</td>
<td>22</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>11.672</td>
<td>0</td>
<td>14.359</td>
<td>-1.2432</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+197A>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0568181818182</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 197, 'AGAP004707-PA', -3506)</td>
<td>('INTRONIC', 'AGAP004707-PB', 197, 'AGAP004707-PB', -3506)</td>
<td>('INTRONIC', 'AGAP004707-PC', 197, 'AGAP004707-PC', -3506)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '2j', -1139)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
<td>('INTRONIC', '1', 197, '2j', -1139)</td>
<td>('INTRONIC', '1', 197, '3', -3488)</td>
</tr>
<tr>
<td>2L</td>
<td>2358536</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>4</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>3</td>
<td>25</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.3203</td>
<td>1</td>
<td>17.234</td>
<td>2.2852</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+232T>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00727272727273</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 232, 'AGAP004707-PA', -3471)</td>
<td>('INTRONIC', 'AGAP004707-PB', 232, 'AGAP004707-PB', -3471)</td>
<td>('INTRONIC', 'AGAP004707-PC', 232, 'AGAP004707-PC', -3471)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '2j', -1104)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
<td>('INTRONIC', '1', 232, '2j', -1104)</td>
<td>('INTRONIC', '1', 232, '3', -3453)</td>
</tr>
<tr>
<td>2L</td>
<td>2358560</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>2</td>
<td>21</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>0</td>
<td>16.109</td>
<td>0.40991</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+256C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 256, 'AGAP004707-PA', -3447)</td>
<td>('INTRONIC', 'AGAP004707-PB', 256, 'AGAP004707-PB', -3447)</td>
<td>('INTRONIC', 'AGAP004707-PC', 256, 'AGAP004707-PC', -3447)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '2j', -1080)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
<td>('INTRONIC', '1', 256, '2j', -1080)</td>
<td>('INTRONIC', '1', 256, '3', -3429)</td>
</tr>
<tr>
<td>2L</td>
<td>2358581</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>330</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>2</td>
<td>20</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.20801</td>
<td>1</td>
<td>21.109</td>
<td>-0.3811</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+277T>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.525454545455</td>
<td style='text-align: right'>0.366071428571</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 277, 'AGAP004707-PA', -3426)</td>
<td>('INTRONIC', 'AGAP004707-PB', 277, 'AGAP004707-PB', -3426)</td>
<td>('INTRONIC', 'AGAP004707-PC', 277, 'AGAP004707-PC', -3426)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '2j', -1059)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
<td>('INTRONIC', '1', 277, '2j', -1059)</td>
<td>('INTRONIC', '1', 277, '3', -3408)</td>
</tr>
<tr>
<td>2L</td>
<td>2358591</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>4</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>4</td>
<td>18</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9912</td>
<td>1</td>
<td>15.461</td>
<td>-0.50586</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+287G>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0326086956522</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 287, 'AGAP004707-PA', -3416)</td>
<td>('INTRONIC', 'AGAP004707-PB', 287, 'AGAP004707-PB', -3416)</td>
<td>('INTRONIC', 'AGAP004707-PC', 287, 'AGAP004707-PC', -3416)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '2j', -1049)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
<td>('INTRONIC', '1', 287, '2j', -1049)</td>
<td>('INTRONIC', '1', 287, '3', -3398)</td>
</tr>
<tr>
<td>2L</td>
<td>2358621</td>
<td>2</td>
<td>G</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>8</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>7.3477</td>
<td>1</td>
<td>14.0</td>
<td>-1.6348</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+317G>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0217391304348</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 317, 'AGAP004707-PA', -3386)</td>
<td>('INTRONIC', 'AGAP004707-PB', 317, 'AGAP004707-PB', -3386)</td>
<td>('INTRONIC', 'AGAP004707-PC', 317, 'AGAP004707-PC', -3386)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '2j', -1019)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
<td>('INTRONIC', '1', 317, '2j', -1019)</td>
<td>('INTRONIC', '1', 317, '3', -3368)</td>
</tr>
<tr>
<td>2L</td>
<td>2358667</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>473</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>11</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.56299</td>
<td>0</td>
<td>30.047</td>
<td>0.18506</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+363T>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.833333333333</td>
<td style='text-align: right'>0.840579710145</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>0.993827160494</td>
<td style='text-align: right'>0.06</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 363, 'AGAP004707-PA', -3340)</td>
<td>('INTRONIC', 'AGAP004707-PB', 363, 'AGAP004707-PB', -3340)</td>
<td>('INTRONIC', 'AGAP004707-PC', 363, 'AGAP004707-PC', -3340)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '2j', -973)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
<td>('INTRONIC', '1', 363, '2j', -973)</td>
<td>('INTRONIC', '1', 363, '3', -3322)</td>
</tr>
<tr>
<td>2L</td>
<td>2358668</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>7</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>12</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>28.266</td>
<td>0</td>
<td>1.8604</td>
<td>-0.94482</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+364G>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.00833333333333</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0326086956522</td>
<td style='text-align: right'>0.0161290322581</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 364, 'AGAP004707-PA', -3339)</td>
<td>('INTRONIC', 'AGAP004707-PB', 364, 'AGAP004707-PB', -3339)</td>
<td>('INTRONIC', 'AGAP004707-PC', 364, 'AGAP004707-PC', -3339)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '2j', -972)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
<td>('INTRONIC', '1', 364, '2j', -972)</td>
<td>('INTRONIC', '1', 364, '3', -3321)</td>
</tr>
<tr>
<td>2L</td>
<td>2358707</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>39</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>12</td>
<td>15</td>
<td>0</td>
<td>1</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>41.875</td>
<td>0</td>
<td>16.781</td>
<td>4.9414</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+403T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.423913043478</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 403, 'AGAP004707-PA', -3300)</td>
<td>('INTRONIC', 'AGAP004707-PB', 403, 'AGAP004707-PB', -3300)</td>
<td>('INTRONIC', 'AGAP004707-PC', 403, 'AGAP004707-PC', -3300)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '2j', -933)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
<td>('INTRONIC', '1', 403, '2j', -933)</td>
<td>('INTRONIC', '1', 403, '3', -3282)</td>
</tr>
<tr>
<td>2L</td>
<td>2358709</td>
<td>2</td>
<td>A</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>12</td>
<td>16</td>
<td>0</td>
<td>1</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.3906</td>
<td>0</td>
<td>12.797</td>
<td>-1.2656</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+405A>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 405, 'AGAP004707-PA', -3298)</td>
<td>('INTRONIC', 'AGAP004707-PB', 405, 'AGAP004707-PB', -3298)</td>
<td>('INTRONIC', 'AGAP004707-PC', 405, 'AGAP004707-PC', -3298)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '2j', -931)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
<td>('INTRONIC', '1', 405, '2j', -931)</td>
<td>('INTRONIC', '1', 405, '3', -3280)</td>
</tr>
<tr>
<td>2L</td>
<td>2358716</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>False</td>
<td>0</td>
<td>9</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>25.453</td>
<td>0</td>
<td>1.0596</td>
<td>-2.9727</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+412T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 412, 'AGAP004707-PA', -3291)</td>
<td>('INTRONIC', 'AGAP004707-PB', 412, 'AGAP004707-PB', -3291)</td>
<td>('INTRONIC', 'AGAP004707-PC', 412, 'AGAP004707-PC', -3291)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '2j', -924)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
<td>('INTRONIC', '1', 412, '2j', -924)</td>
<td>('INTRONIC', '1', 412, '3', -3273)</td>
</tr>
<tr>
<td>2L</td>
<td>2358734</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>9</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>6.4297</td>
<td>1</td>
<td>16.016</td>
<td>-0.42896</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+430C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00363636363636</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 430, 'AGAP004707-PA', -3273)</td>
<td>('INTRONIC', 'AGAP004707-PB', 430, 'AGAP004707-PB', -3273)</td>
<td>('INTRONIC', 'AGAP004707-PC', 430, 'AGAP004707-PC', -3273)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '2j', -906)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
<td>('INTRONIC', '1', 430, '2j', -906)</td>
<td>('INTRONIC', '1', 430, '3', -3255)</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>


## Add LD with kdr mutations

### Setup haplotype data


```python
# these are the biallelics phased with shapeit2
callset_vgsc_phased = h5py.File('../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3.1/haplotypes/specific_regions/PARA/2L_2358158_2431617.h5', mode='r')
callset_vgsc_phased
```




    <HDF5 file "2L_2358158_2431617.h5" (mode r)>




```python
# positions of all biallelic SNPs in the shapeit2 callset
pos_biallelic = allel.SortedIndex(callset_vgsc_phased['2L/variants/POS'])
pos_biallelic
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(1967,) dtype=int32&gt;</span><table><tr><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1962</th><th style="text-align: center">1963</th><th style="text-align: center">1964</th><th style="text-align: center">1965</th><th style="text-align: center">1966</th></tr><tr><td style="text-align: center">2353212</td><td style="text-align: center">2353223</td><td style="text-align: center">2353234</td><td style="text-align: center">2353251</td><td style="text-align: center">2353288</td><td style="text-align: center">...</td><td style="text-align: center">2436544</td><td style="text-align: center">2436545</td><td style="text-align: center">2436558</td><td style="text-align: center">2436585</td><td style="text-align: center">2436615</td></tr></table></div>




```python
# N.B., exclude cross parents (last 16 haplotypes)
haplotypes_biallelic = allel.GenotypeArray(callset_vgsc_phased['2L/calldata/genotype']).to_haplotypes()[:, :1530]
haplotypes_biallelic
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(1967, 1530) dtype=int8&gt;</span><table><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr><tr><th style="text-align: center">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center">1964</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1965</th><td style="text-align: center">1</td><td style="text-align: center">1</td><td style="text-align: center">0</td><td style="text-align: center">1</td><td style="text-align: center">1</td><td style="text-align: center">...</td><td style="text-align: center">1</td><td style="text-align: center">1</td><td style="text-align: center">1</td><td style="text-align: center">1</td><td style="text-align: center">1</td></tr><tr><th style="text-align: center">1966</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></table></div>




```python
# these are the multiallelics phased with mvncall
callset_vgsc_phased_multiallelics = np.load('../data/missense_multiallelics.mvncall.200.npz')
callset_vgsc_phased_multiallelics
```




    <numpy.lib.npyio.NpzFile at 0x7f0d514ccac8>




```python
# positions of multiallelic SNPs in the mvncall callset
pos_multiallelic = allel.SortedIndex(callset_vgsc_phased_multiallelics['variants']['POS'])
pos_multiallelic
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(2,) dtype=int32&gt;</span><table><tr><th style="text-align: center">0</th><th style="text-align: center">1</th></tr><tr><td style="text-align: center">2391228</td><td style="text-align: center">2400071</td></tr></table></div>




```python
# haplotypes at all phased multiallelic sites
haplotypes_multiallelic = allel.GenotypeArray(callset_vgsc_phased_multiallelics['calldata']['genotype']).to_haplotypes()
haplotypes_multiallelic
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(2, 1530) dtype=int8&gt;</span><table><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr><tr><th style="text-align: center">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">2</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></table></div>




```python
# combine haplotypes for bi- and multi-allelic SNPs: just add multiallelics on at the end
haplotypes_combined = haplotypes_biallelic.concatenate(haplotypes_multiallelic)
haplotypes_combined
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(1969, 1530) dtype=int8&gt;</span><table><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr><tr><th style="text-align: center">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center">1966</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1967</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">2</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center">1968</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></table></div>




```python
pos_combined = list(pos_biallelic) + list(pos_multiallelic)
pos_combined[:5], len(pos_combined)
```




    ([2353212, 2353223, 2353234, 2353251, 2353288], 1969)



### Add LD columns


```python
def lewontin_d_prime(h, i, j, a=1, b=1):
    
    # setup
    h = allel.HaplotypeArray(h)
    n_a = n_b = 0  # allele counts
    n_ab = 0  # haplotype counts
    n = 0  # allele number (i.e., number of calls)
    
    # iterate over haplotypes, counting alleles and haplotypes
    for k in range(h.n_haplotypes):
        
        # access alleles
        allele_ik = h[i, k]
        allele_jk = h[j, k]
        
        # only count if allele non-missing at both sites
        if allele_ik < 0 or allele_jk < 0:
            continue
            
        # accumulate
        if allele_ik == a:
            n_a += 1
        if allele_jk == b:
            n_b += 1
        if allele_ik == a and allele_jk == b:
            n_ab += 1
        n += 1
        
    # bail out if no data or either allele is absent or fixed
    if n == 0 or n_a == 0 or n_b == 0 or n == n_a or n == n_b:
        return None
    
    # N.B., compute D prime using counts rather than frequencies to avoid floating-point errors
    # N.B., preserve the sign of D prime to retain information about linkage versus repulsion
    
    # compute coefficient of linkage disequilibrium * n**2
    D_ab = (n * n_ab) - (n_a * n_b)
    
    # compute normalisation coefficient * n**2
    if D_ab >= 0:
        D_max = min(n_a * (n - n_b), (n - n_a) * n_b)
    else:
        D_max = min(n_a * n_b, (n - n_a) * (n - n_b))

    # compute D prime
    return D_ab / D_max

```


```python
def _list_index(l, i):
    try:
        return l.index(i)
    except ValueError:
        return None
    
    
def _mkfield_dprime(i):
    def _f(row):
        if row.haps_vidx is not None:
            return lewontin_d_prime(haplotypes_combined, i=i, j=row.haps_vidx, a=1, b=row.ALTIX+1)  
        else:
            return None
    return _f

tbl_variants_phase1_eff_ld = (
    tbl_variants_phase1_eff
    .addfield('haps_vidx', lambda row: _list_index(pos_combined, row['POS']))
    .addfield('dprime_L995S', _mkfield_dprime(1613))
    .addfield('dprime_L995F', _mkfield_dprime(1614))  
    .cache()
)
tbl_variants_phase1_eff_ld
```




<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
<th>51|haps_vidx</th>
<th>52|dprime_L995S</th>
<th>53|dprime_L995F</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2358158</td>
<td style='text-align: right'>2358304</td>
<td>1</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td style='text-align: right'>83</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358316</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>73</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4844</td>
<td>0</td>
<td>16.438</td>
<td>1.4219</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+12T>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.132727272727</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 12, 'AGAP004707-PA', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PB', 12, 'AGAP004707-PB', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PC', 12, 'AGAP004707-PC', -3691)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td style='text-align: right'>84</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358328</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.7363</td>
<td>0</td>
<td>16.062</td>
<td>-0.646</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+24T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 24, 'AGAP004707-PA', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PB', 24, 'AGAP004707-PB', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PC', 24, 'AGAP004707-PC', -3679)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td style='text-align: right'>85</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358353</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9512</td>
<td>0</td>
<td>9.8594</td>
<td>1.1582</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+49C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 49, 'AGAP004707-PA', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PB', 49, 'AGAP004707-PB', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PC', 49, 'AGAP004707-PC', -3654)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td style='text-align: right'>86</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358405</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>6</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.844</td>
<td>1</td>
<td>10.859</td>
<td>1.1562</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+101T>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 101, 'AGAP004707-PA', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PB', 101, 'AGAP004707-PB', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PC', 101, 'AGAP004707-PC', -3602)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td style='text-align: right'>87</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>



## Inspect missense variants


```python
def simplify_missense_effect(v):
    if v and v[0] == 'NON_SYNONYMOUS_CODING':
        return v[1]
    else:
        return ''

    
td_styles = {
    'FILTER_PASS': lambda v: 'background-color: red' if not v else '',
    'NoCoverage': lambda v: 'background-color: red' if v > 1 else '',
    'LowCoverage': lambda v: 'background-color: red' if v > 76 else '',
    'HighCoverage': lambda v: 'background-color: red' if v > 15 else '',
    'LowMQ': lambda v: 'background-color: red' if v > 76 else '',
    'HighMQ0': lambda v: 'background-color: red' if v > 1 else '',
    'RepeatDUST': lambda v: 'background-color: red' if v else '',
    'FS': lambda v: 'background-color: red' if v > 60 else '',
    'QD': lambda v: 'background-color: red' if v < 5 else '',
    'ReadPosRankSum': lambda v: 'background-color: red' if v < -8 else '',
    'HRun': lambda v: 'background-color: red' if v > 4 else '',
    'num_alleles': lambda v: 'background-color: orange' if v > 2 else '',
}


def tr_style(row):
    """Colour row by alternate allele count."""
    return 'background-color:rgba(0, 255, 0, %.3f)' % (min(1, row['AC']/100))


tbl_variants_phase1_missense = (
    tbl_variants_phase1_eff_ld
    .select(lambda row: any(row[t] and row[t][0] == 'NON_SYNONYMOUS_CODING' for t in transcript_ids))
    .convert(transcript_ids, simplify_missense_effect)
)
tbl_variants_phase1_missense.displayall(td_styles=td_styles, tr_style=tr_style)
```


<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
<th>51|haps_vidx</th>
<th>52|dprime_L995S</th>
<th>53|dprime_L995F</th>
</tr>
</thead>
<tbody>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2358158</td>
<td style='text-align: right'>2358304</td>
<td>1</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td>D33N</td>
<td style='text-align: right'>83</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.070)'>
<td>2L</td>
<td>2359670</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>7</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>1</td>
<td style='background-color: red'>171</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>8.6641</td>
<td style='background-color: red'>6</td>
<td>14.406</td>
<td>-0.029007</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+1366G></td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0109090909091</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0113636363636</td>
<td>True</td>
<td style='text-align: right'>2359640</td>
<td style='text-align: right'>2359672</td>
<td>2j</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>E60K</td>
<td></td>
<td></td>
<td></td>
<td>E60K</td>
<td></td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2362002</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.5459</td>
<td>0</td>
<td>12.531</td>
<td>-0.55322</td>
<td>T</td>
<td>splice_region_variant&intron_varia</td>
<td>n.148-5A>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
<td></td>
<td></td>
<td></td>
<td>D54V</td>
<td>D54V</td>
<td>D54V</td>
<td>D54V</td>
<td>D65V</td>
<td>D54V</td>
<td>D54V</td>
<td>D54V</td>
<td>D65V</td>
<td>D54V</td>
<td style='text-align: right'>223</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2362019</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.9824</td>
<td>0</td>
<td>13.641</td>
<td>0.7749</td>
<td>T</td>
<td>missense_variant</td>
<td>n.160G>T</td>
<td>p.Gly54Cys</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
<td>G54C</td>
<td>G54C</td>
<td>G54C</td>
<td>G60C</td>
<td>G60C</td>
<td>G60C</td>
<td>G60C</td>
<td>G71C</td>
<td>G60C</td>
<td>G60C</td>
<td>G60C</td>
<td>G71C</td>
<td>G60C</td>
<td style='text-align: right'>225</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2362023</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>0</td>
<td>13.477</td>
<td>-1.1611</td>
<td>T</td>
<td>missense_variant</td>
<td>n.164C>T</td>
<td>p.Pro55Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
<td>P55L</td>
<td>P55L</td>
<td>P55L</td>
<td>P61L</td>
<td>P61L</td>
<td>P61L</td>
<td>P61L</td>
<td>P72L</td>
<td>P61L</td>
<td>P61L</td>
<td>P61L</td>
<td>P72L</td>
<td>P61L</td>
<td style='text-align: right'>226</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2390168</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.56982</td>
<td>1</td>
<td>15.219</td>
<td>-0.026001</td>
<td>G</td>
<td>missense_variant</td>
<td>n.752A>G</td>
<td>p.Lys251Arg</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0178571428571</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2390129</td>
<td style='text-align: right'>2390341</td>
<td>7</td>
<td>K251R</td>
<td>K251R</td>
<td>K251R</td>
<td>K257R</td>
<td>K214R</td>
<td>K257R</td>
<td>K257R</td>
<td>K268R</td>
<td>K257R</td>
<td>K257R</td>
<td>K257R</td>
<td>K268R</td>
<td>K257R</td>
<td style='text-align: right'>899</td>
<td style='text-align: right'>0.30454545454545456</td>
<td style='text-align: right'>-0.012903225806451613</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2390177</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>198</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>3</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.12695</td>
<td>1</td>
<td>18.625</td>
<td>0.83496</td>
<td>A</td>
<td>missense_variant</td>
<td>n.761G>A</td>
<td>p.Arg254Lys</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.316363636364</td>
<td style='text-align: right'>0.214285714286</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2390129</td>
<td style='text-align: right'>2390341</td>
<td>7</td>
<td>R254K</td>
<td>R254K</td>
<td>R254K</td>
<td>R260K</td>
<td>R217K</td>
<td>R260K</td>
<td>R260K</td>
<td>R271K</td>
<td>R260K</td>
<td>R260K</td>
<td>R260K</td>
<td>R271K</td>
<td>R260K</td>
<td style='text-align: right'>900</td>
<td style='text-align: right'>-0.9820295983086681</td>
<td style='text-align: right'>0.9590608067429259</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2390311</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>3</td>
<td>14.07</td>
<td>-0.70996</td>
<td>A</td>
<td>missense_variant</td>
<td>n.895G>A</td>
<td>p.Glu299Lys</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2390129</td>
<td style='text-align: right'>2390341</td>
<td>7</td>
<td>E299K</td>
<td>E299K</td>
<td>E299K</td>
<td>E305K</td>
<td>E262K</td>
<td>E305K</td>
<td>E305K</td>
<td>E316K</td>
<td>E305K</td>
<td>E305K</td>
<td>E305K</td>
<td>E316K</td>
<td>E305K</td>
<td style='text-align: right'>904</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.060)'>
<td>2L</td>
<td>2390448</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>6</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.71094</td>
<td>0</td>
<td>16.125</td>
<td>-0.65918</td>
<td>A</td>
<td>missense_variant</td>
<td>n.949G>A</td>
<td>p.Gly317Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0109090909091</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2390425</td>
<td style='text-align: right'>2390485</td>
<td>8</td>
<td>G317S</td>
<td>G317S</td>
<td>G317S</td>
<td>G323S</td>
<td>G280S</td>
<td>G323S</td>
<td>G323S</td>
<td>G334S</td>
<td>G323S</td>
<td>G323S</td>
<td>G323S</td>
<td>G334S</td>
<td>G323S</td>
<td style='text-align: right'>911</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.100)'>
<td>2L</td>
<td>2391228</td>
<td style='background-color: orange'>3</td>
<td>G</td>
<td>C</td>
<td>10</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>12</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.0352</td>
<td>0</td>
<td>14.867</td>
<td>-1.1777</td>
<td>C</td>
<td>missense_variant</td>
<td>n.1204G>C</td>
<td>p.Val402Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0724637681159</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2391156</td>
<td style='text-align: right'>2391320</td>
<td>10</td>
<td>V402L</td>
<td>V402L</td>
<td>V402L</td>
<td>V408L</td>
<td>V365L</td>
<td></td>
<td>V408L</td>
<td>V419L</td>
<td>V408L</td>
<td>V408L</td>
<td>V408L</td>
<td>V419L</td>
<td>V408L</td>
<td style='text-align: right'>1967</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.40774193548387094</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.090)'>
<td>2L</td>
<td>2391228</td>
<td style='background-color: orange'>3</td>
<td>G</td>
<td>T</td>
<td>9</td>
<td style='text-align: right'>1</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>12</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.0352</td>
<td>0</td>
<td>14.867</td>
<td>-1.1777</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0652173913043</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2391156</td>
<td style='text-align: right'>2391320</td>
<td>10</td>
<td>V402L</td>
<td>V402L</td>
<td>V402L</td>
<td>V408L</td>
<td>V365L</td>
<td></td>
<td>V408L</td>
<td>V419L</td>
<td>V408L</td>
<td>V408L</td>
<td>V408L</td>
<td>V419L</td>
<td>V408L</td>
<td style='text-align: right'>1967</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.09933774834437085</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.380)'>
<td>2L</td>
<td>2399997</td>
<td>2</td>
<td>G</td>
<td>C</td>
<td>38</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>13.359</td>
<td>0</td>
<td>15.688</td>
<td>0.11798</td>
<td>C</td>
<td>missense_variant</td>
<td>n.1396G>C</td>
<td>p.Asp466His</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0690909090909</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2399898</td>
<td style='text-align: right'>2400173</td>
<td>11i+</td>
<td>D466H</td>
<td>D466H</td>
<td>D466H</td>
<td>D472H</td>
<td>D429H</td>
<td>D417H</td>
<td>D472H</td>
<td>D483H</td>
<td>D472H</td>
<td>D472H</td>
<td>D472H</td>
<td>D483H</td>
<td>D472H</td>
<td style='text-align: right'>1162</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.160)'>
<td>2L</td>
<td>2400071</td>
<td style='background-color: orange'>3</td>
<td>G</td>
<td>A</td>
<td>16</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.6875</td>
<td>0</td>
<td>16.969</td>
<td>1.3232</td>
<td>A</td>
<td>missense_variant</td>
<td>n.1470G>A</td>
<td>p.Met490Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.181818181818</td>
<td>True</td>
<td style='text-align: right'>2399898</td>
<td style='text-align: right'>2400173</td>
<td>11i+</td>
<td>M490I</td>
<td>M490I</td>
<td>M490I</td>
<td>M496I</td>
<td>M453I</td>
<td>M441I</td>
<td>M496I</td>
<td>M507I</td>
<td>M496I</td>
<td>M496I</td>
<td>M496I</td>
<td>M507I</td>
<td>M496I</td>
<td style='text-align: right'>1968</td>
<td style='text-align: right'>-0.3328488372093023</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2400071</td>
<td style='background-color: orange'>3</td>
<td>G</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>1</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.6875</td>
<td>0</td>
<td>16.969</td>
<td>1.3232</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00363636363636</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2399898</td>
<td style='text-align: right'>2400173</td>
<td>11i+</td>
<td>M490I</td>
<td>M490I</td>
<td>M490I</td>
<td>M496I</td>
<td>M453I</td>
<td>M441I</td>
<td>M496I</td>
<td>M507I</td>
<td>M496I</td>
<td>M496I</td>
<td>M496I</td>
<td>M507I</td>
<td>M496I</td>
<td style='text-align: right'>1968</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.012903225806451613</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2400076</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.1055</td>
<td>1</td>
<td>10.469</td>
<td>-0.54199</td>
<td>A</td>
<td>missense_variant</td>
<td>n.1475T>A</td>
<td>p.Ile492Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00970873786408</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2399898</td>
<td style='text-align: right'>2400173</td>
<td>11i+</td>
<td>I492N</td>
<td>I492N</td>
<td>I492N</td>
<td>I498N</td>
<td>I455N</td>
<td>I443N</td>
<td>I498N</td>
<td>I509N</td>
<td>I498N</td>
<td>I498N</td>
<td>I498N</td>
<td>I509N</td>
<td>I498N</td>
<td style='text-align: right'>1165</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2402484</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>4</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.8857</td>
<td>1</td>
<td>14.719</td>
<td>0.075989</td>
<td>T</td>
<td>missense_variant</td>
<td>n.1610G>T</td>
<td>p.Arg537Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00892857142857</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2402447</td>
<td style='text-align: right'>2402509</td>
<td>13a</td>
<td>R537L</td>
<td>R537L</td>
<td>R537L</td>
<td>R550L</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>R550L</td>
<td></td>
<td>R550L</td>
<td style='text-align: right'>1217</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2402508</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>1</td>
<td>3</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.0098</td>
<td>0</td>
<td>11.156</td>
<td>-0.041992</td>
<td>T</td>
<td>missense_variant&splice_region_var</td>
<td>n.1634A>T</td>
<td>p.Gln545Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2402447</td>
<td style='text-align: right'>2402509</td>
<td>13a</td>
<td>Q545L</td>
<td>Q545L</td>
<td>Q545L</td>
<td>Q558L</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Q558L</td>
<td></td>
<td>Q558L</td>
<td style='text-align: right'>1218</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2403206</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>1</td>
<td style='background-color: red'>16</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.8047</td>
<td>0</td>
<td>15.477</td>
<td>-0.20398</td>
<td>A</td>
<td>missense_variant</td>
<td>n.1756G>A</td>
<td>p.Ala586Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2403086</td>
<td style='text-align: right'>2403269</td>
<td>14</td>
<td>A586T</td>
<td>A586T</td>
<td>A586T</td>
<td>A599T</td>
<td>A528T</td>
<td>A516T</td>
<td>A571T</td>
<td>A582T</td>
<td>A571T</td>
<td>A571T</td>
<td>A599T</td>
<td>A582T</td>
<td>A599T</td>
<td style='text-align: right'>1235</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2407811</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>1</td>
<td>10.789</td>
<td>-0.86914</td>
<td>A</td>
<td>missense_variant</td>
<td>n.2009G>A</td>
<td>p.Arg670Gln</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2407622</td>
<td style='text-align: right'>2407818</td>
<td>15</td>
<td>R670Q</td>
<td>R670Q</td>
<td>R670Q</td>
<td>R683Q</td>
<td>R612Q</td>
<td>R600Q</td>
<td>R655Q</td>
<td>R666Q</td>
<td>R655Q</td>
<td>R655Q</td>
<td>R683Q</td>
<td>R666Q</td>
<td>R683Q</td>
<td style='text-align: right'>1295</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2407912</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>1</td>
<td>22.172</td>
<td>0.5332</td>
<td>T</td>
<td>missense_variant</td>
<td>n.2035A>T</td>
<td>p.Thr679Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2407894</td>
<td style='text-align: right'>2407993</td>
<td>16</td>
<td>T679S</td>
<td>T679S</td>
<td>T679S</td>
<td>T692S</td>
<td>T621S</td>
<td>T609S</td>
<td>T664S</td>
<td>T675S</td>
<td>T664S</td>
<td>T664S</td>
<td>T692S</td>
<td>T675S</td>
<td>T692S</td>
<td style='text-align: right'>1299</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2407987</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>0</td>
<td>14.102</td>
<td>1.0859</td>
<td>G</td>
<td>missense_variant</td>
<td>n.2110A>G</td>
<td>p.Met704Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2407894</td>
<td style='text-align: right'>2407993</td>
<td>16</td>
<td>M704V</td>
<td>M704V</td>
<td>M704V</td>
<td>M717V</td>
<td>M646V</td>
<td>M634V</td>
<td>M689V</td>
<td>M700V</td>
<td>M689V</td>
<td>M689V</td>
<td>M717V</td>
<td>M700V</td>
<td>M717V</td>
<td style='text-align: right'>1300</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2408125</td>
<td>2</td>
<td>C</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td style='background-color: red'>252</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.0879</td>
<td>2</td>
<td>7.0586</td>
<td>0.5918</td>
<td>A</td>
<td>missense_variant</td>
<td>n.2171C>A</td>
<td>p.Ala724Glu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2408071</td>
<td style='text-align: right'>2408139</td>
<td>17</td>
<td>A724E</td>
<td>A724E</td>
<td>A724E</td>
<td>A737E</td>
<td>A666E</td>
<td>A654E</td>
<td>A709E</td>
<td>A720E</td>
<td>A709E</td>
<td>A709E</td>
<td>A737E</td>
<td>A720E</td>
<td>A737E</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2408136</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td style='background-color: red'>318</td>
<td>2</td>
<td>1</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.0879</td>
<td>0</td>
<td style='background-color: red'>1.8799</td>
<td>-2.0742</td>
<td>A</td>
<td>missense_variant</td>
<td>n.2182G>A</td>
<td>p.Gly728Arg</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.00833333333333</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2408071</td>
<td style='text-align: right'>2408139</td>
<td>17</td>
<td>G728R</td>
<td>G728R</td>
<td>G728R</td>
<td>G741R</td>
<td>G670R</td>
<td>G658R</td>
<td>G713R</td>
<td>G724R</td>
<td>G713R</td>
<td>G713R</td>
<td>G741R</td>
<td>G724R</td>
<td>G741R</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.320)'>
<td>2L</td>
<td>2416980</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>32</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>11</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.0449</td>
<td>0</td>
<td>17.703</td>
<td>0.37305</td>
<td>T</td>
<td>missense_variant</td>
<td>n.2372C>T</td>
<td>p.Thr791Met</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.129032258065</td>
<td style='text-align: right'>0.135802469136</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2416794</td>
<td style='text-align: right'>2417071</td>
<td>18b+</td>
<td>T791M</td>
<td>T791M</td>
<td>T791M</td>
<td>T804M</td>
<td>T733M</td>
<td>T721M</td>
<td>T776M</td>
<td>T787M</td>
<td>T776M</td>
<td>T776M</td>
<td>T804M</td>
<td>T787M</td>
<td>T804M</td>
<td style='text-align: right'>1516</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2417206</td>
<td>2</td>
<td>A</td>
<td>C</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>15</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>2</td>
<td>9.4297</td>
<td>0.31299</td>
<td>C</td>
<td>missense_variant</td>
<td>n.2485A>C</td>
<td>p.Ile829Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2417185</td>
<td style='text-align: right'>2417358</td>
<td>19</td>
<td>I829L</td>
<td>I829L</td>
<td>I829L</td>
<td>I842L</td>
<td>I771L</td>
<td>I759L</td>
<td>I814L</td>
<td>I825L</td>
<td>I814L</td>
<td>I814L</td>
<td>I842L</td>
<td>I825L</td>
<td>I842L</td>
<td style='text-align: right'>1530</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2417231</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>38</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.6992</td>
<td>0</td>
<td>13.688</td>
<td>-0.46802</td>
<td>T</td>
<td>missense_variant</td>
<td>n.2510C>T</td>
<td>p.Ala837Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2417185</td>
<td style='text-align: right'>2417358</td>
<td>19</td>
<td>A837V</td>
<td>A837V</td>
<td>A837V</td>
<td>A850V</td>
<td>A779V</td>
<td>A767V</td>
<td>A822V</td>
<td>A833V</td>
<td>A822V</td>
<td>A822V</td>
<td>A850V</td>
<td>A833V</td>
<td>A850V</td>
<td style='text-align: right'>1531</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2417772</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>7.707</td>
<td>1</td>
<td>16.156</td>
<td>-0.035004</td>
<td>T</td>
<td>missense_variant</td>
<td>n.2773A>T</td>
<td>p.Met925Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00485436893204</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2417637</td>
<td style='text-align: right'>2417799</td>
<td>20c</td>
<td>M925L</td>
<td></td>
<td>M925L</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>M938L</td>
<td style='text-align: right'>1537</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2421454</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.8008</td>
<td>1</td>
<td>14.094</td>
<td>0.88916</td>
<td>G</td>
<td>intron_variant</td>
<td>n.2801-1014A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2421385</td>
<td style='text-align: right'>2421547</td>
<td>20d</td>
<td></td>
<td>M903V</td>
<td></td>
<td>M916V</td>
<td>M845V</td>
<td>M833V</td>
<td>M888V</td>
<td>M899V</td>
<td>M888V</td>
<td>M888V</td>
<td>M916V</td>
<td>M899V</td>
<td></td>
<td style='text-align: right'>1598</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2422486</td>
<td>2</td>
<td>C</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.168</td>
<td>0</td>
<td>12.102</td>
<td>-0.45605</td>
<td>A</td>
<td>missense_variant</td>
<td>n.2819C>A</td>
<td>p.Pro940His</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2422468</td>
<td style='text-align: right'>2422655</td>
<td>21</td>
<td>P940H</td>
<td>P940H</td>
<td>P940H</td>
<td>P953H</td>
<td>P882H</td>
<td>P870H</td>
<td>P925H</td>
<td>P936H</td>
<td>P925H</td>
<td>P925H</td>
<td>P953H</td>
<td>P936H</td>
<td>P953H</td>
<td style='text-align: right'>1611</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2422651</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>430</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.95117</td>
<td>0</td>
<td>27.203</td>
<td>-0.92822</td>
<td>C</td>
<td>missense_variant</td>
<td>n.2984T>C</td>
<td>p.Leu995Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.154545454545</td>
<td style='text-align: right'>0.642857142857</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>0.761363636364</td>
<td>True</td>
<td style='text-align: right'>2422468</td>
<td style='text-align: right'>2422655</td>
<td>21</td>
<td>L995S</td>
<td>L995S</td>
<td>L995S</td>
<td>L1008S</td>
<td>L937S</td>
<td>L925S</td>
<td>L980S</td>
<td>L991S</td>
<td>L980S</td>
<td>L980S</td>
<td>L1008S</td>
<td>L991S</td>
<td>L1008S</td>
<td style='text-align: right'>1613</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2422652</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>775</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.73291</td>
<td>3</td>
<td>29.047</td>
<td>0.19104</td>
<td>T</td>
<td>missense_variant</td>
<td>n.2985A>T</td>
<td>p.Leu995Phe</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.858333333333</td>
<td style='text-align: right'>0.847826086957</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>0.529090909091</td>
<td style='text-align: right'>0.357142857143</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2422468</td>
<td style='text-align: right'>2422655</td>
<td>21</td>
<td>L995F</td>
<td>L995F</td>
<td>L995F</td>
<td>L1008F</td>
<td>L937F</td>
<td>L925F</td>
<td>L980F</td>
<td>L991F</td>
<td>L980F</td>
<td>L980F</td>
<td>L1008F</td>
<td>L991F</td>
<td>L1008F</td>
<td style='text-align: right'>1614</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2422875</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>3</td>
<td style='background-color: red'>17</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.71289</td>
<td>0</td>
<td>14.867</td>
<td>-1.6621</td>
<td>A</td>
<td>missense_variant</td>
<td>n.3151G>A</td>
<td>p.Val1051Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2422713</td>
<td style='text-align: right'>2422920</td>
<td>22</td>
<td>V1051I</td>
<td>V1051I</td>
<td>V1051I</td>
<td>V1064I</td>
<td>V993I</td>
<td>V981I</td>
<td>V1036I</td>
<td>V1047I</td>
<td>V1036I</td>
<td>V1036I</td>
<td>V1064I</td>
<td>V1047I</td>
<td>V1064I</td>
<td style='text-align: right'>1617</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2424383</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.8906</td>
<td>0</td>
<td>18.156</td>
<td>-0.31494</td>
<td>T</td>
<td>missense_variant</td>
<td>n.3373G>T</td>
<td>p.Ala1125Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2424207</td>
<td style='text-align: right'>2424418</td>
<td>23f+</td>
<td>A1125S</td>
<td>A1125S</td>
<td>A1125S</td>
<td>A1138S</td>
<td>A1067S</td>
<td>A1045S</td>
<td>A1100S</td>
<td>A1121S</td>
<td>A1110S</td>
<td>A1110S</td>
<td>A1138S</td>
<td>A1121S</td>
<td>A1138S</td>
<td style='text-align: right'>1647</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.110)'>
<td>2L</td>
<td>2424384</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>11</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.4141</td>
<td>0</td>
<td>14.172</td>
<td>-2.3242</td>
<td>T</td>
<td>missense_variant</td>
<td>n.3374C>T</td>
<td>p.Ala1125Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0916666666667</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2424207</td>
<td style='text-align: right'>2424418</td>
<td>23f+</td>
<td>A1125V</td>
<td>A1125V</td>
<td>A1125V</td>
<td>A1138V</td>
<td>A1067V</td>
<td>A1045V</td>
<td>A1100V</td>
<td>A1121V</td>
<td>A1110V</td>
<td>A1110V</td>
<td>A1138V</td>
<td>A1121V</td>
<td>A1138V</td>
<td style='text-align: right'>1648</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2424401</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>0</td>
<td style='background-color: red'>16</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.1133</td>
<td>0</td>
<td>14.742</td>
<td>-1.7324</td>
<td>G</td>
<td>missense_variant</td>
<td>n.3391A>G</td>
<td>p.Ile1131Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.00892857142857</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2424207</td>
<td style='text-align: right'>2424418</td>
<td>23f+</td>
<td>I1131V</td>
<td>I1131V</td>
<td>I1131V</td>
<td>I1144V</td>
<td>I1073V</td>
<td>I1051V</td>
<td>I1106V</td>
<td>I1127V</td>
<td>I1116V</td>
<td>I1116V</td>
<td>I1144V</td>
<td>I1127V</td>
<td>I1144V</td>
<td style='text-align: right'>1649</td>
<td style='text-align: right'>0.30454545454545456</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.110)'>
<td>2L</td>
<td>2424720</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>11</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>2</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td style='background-color: red'>1953.0</td>
<td>1</td>
<td style='background-color: red'>0.090027</td>
<td>1.6211</td>
<td>G</td>
<td>missense_variant</td>
<td>n.3478T>G</td>
<td>p.Ser1160Ala</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.00833333333333</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0109090909091</td>
<td style='text-align: right'>0.00892857142857</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2424651</td>
<td style='text-align: right'>2424870</td>
<td>24h+</td>
<td>S1160A</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>S1173A</td>
<td>S1156A</td>
<td>S1173A</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.050)'>
<td>2L</td>
<td>2425077</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>5</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.66992</td>
<td>0</td>
<td>14.891</td>
<td>-0.61816</td>
<td>A</td>
<td>missense_variant</td>
<td>n.3760G>A</td>
<td>p.Val1254Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.054347826087</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2424946</td>
<td style='text-align: right'>2425211</td>
<td>25</td>
<td>V1254I</td>
<td>V1228I</td>
<td>V1228I</td>
<td>V1241I</td>
<td>V1170I</td>
<td>V1148I</td>
<td>V1203I</td>
<td>V1224I</td>
<td>V1213I</td>
<td>V1213I</td>
<td>V1267I</td>
<td>V1250I</td>
<td>V1267I</td>
<td style='text-align: right'>1664</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2425291</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.4258</td>
<td>0</td>
<td>15.32</td>
<td>-0.38403</td>
<td>C</td>
<td>missense_variant</td>
<td>n.3908T>C</td>
<td>p.Val1303Ala</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2425278</td>
<td style='text-align: right'>2425451</td>
<td>26</td>
<td>V1303A</td>
<td>V1277A</td>
<td>V1277A</td>
<td>V1290A</td>
<td>V1219A</td>
<td>V1197A</td>
<td>V1252A</td>
<td>V1273A</td>
<td>V1262A</td>
<td>V1262A</td>
<td>V1316A</td>
<td>V1299A</td>
<td>V1316A</td>
<td style='text-align: right'>1668</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.030)'>
<td>2L</td>
<td>2425417</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>3</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.39111</td>
<td>1</td>
<td>14.141</td>
<td>0.104</td>
<td>T</td>
<td>missense_variant</td>
<td>n.4034A>T</td>
<td>p.Asn1345Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0217391304348</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2425278</td>
<td style='text-align: right'>2425451</td>
<td>26</td>
<td>N1345I</td>
<td>N1319I</td>
<td>N1319I</td>
<td>N1332I</td>
<td>N1261I</td>
<td>N1239I</td>
<td>N1294I</td>
<td>N1315I</td>
<td>N1304I</td>
<td>N1304I</td>
<td>N1358I</td>
<td>N1341I</td>
<td>N1358I</td>
<td style='text-align: right'>1669</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2428015</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>3</td>
<td>12</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.66895</td>
<td>3</td>
<td>13.711</td>
<td>-0.55322</td>
<td>T</td>
<td>missense_variant</td>
<td>n.4096C>T</td>
<td>p.Leu1366Phe</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00617283950617</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2427988</td>
<td style='text-align: right'>2428110</td>
<td>27l</td>
<td>L1366F</td>
<td>L1340F</td>
<td>L1340F</td>
<td>L1353F</td>
<td>L1282F</td>
<td>L1260F</td>
<td>L1315F</td>
<td>L1336F</td>
<td>L1325F</td>
<td>L1325F</td>
<td>L1379F</td>
<td>L1362F</td>
<td></td>
<td style='text-align: right'>1729</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.190)'>
<td>2L</td>
<td>2429617</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>19</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>12</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.4502</td>
<td>0</td>
<td>15.531</td>
<td>-0.98291</td>
<td>C</td>
<td>missense_variant</td>
<td>n.4580T>C</td>
<td>p.Ile1527Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.13768115942</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429556</td>
<td style='text-align: right'>2429801</td>
<td>30</td>
<td>I1527T</td>
<td>I1501T</td>
<td>I1501T</td>
<td>I1511T</td>
<td>I1440T</td>
<td>I1418T</td>
<td>I1473T</td>
<td>I1494T</td>
<td>I1483T</td>
<td>I1483T</td>
<td>I1537T</td>
<td>I1520T</td>
<td>I1537T</td>
<td style='text-align: right'>1755</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2429622</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>10.922</td>
<td>1</td>
<td>14.977</td>
<td>-0.098022</td>
<td>C</td>
<td>missense_variant</td>
<td>n.4585T>C</td>
<td>p.Phe1529Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00485436893204</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429556</td>
<td style='text-align: right'>2429801</td>
<td>30</td>
<td>F1529L</td>
<td>F1503L</td>
<td>F1503L</td>
<td>F1513L</td>
<td>F1442L</td>
<td>F1420L</td>
<td>F1475L</td>
<td>F1496L</td>
<td>F1485L</td>
<td>F1485L</td>
<td>F1539L</td>
<td>F1522L</td>
<td>F1539L</td>
<td style='text-align: right'>1756</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2429745</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>110</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>0</td>
<td style='background-color: red'>17</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.4541</td>
<td>1</td>
<td>16.484</td>
<td>1.9131</td>
<td>T</td>
<td>missense_variant</td>
<td>n.4708A>T</td>
<td>p.Asn1570Tyr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.260869565217</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0967741935484</td>
<td style='text-align: right'>0.216049382716</td>
<td style='text-align: right'>0.06</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429556</td>
<td style='text-align: right'>2429801</td>
<td>30</td>
<td>N1570Y</td>
<td>N1544Y</td>
<td>N1544Y</td>
<td>N1554Y</td>
<td>N1483Y</td>
<td>N1461Y</td>
<td>N1516Y</td>
<td>N1537Y</td>
<td>N1526Y</td>
<td>N1526Y</td>
<td>N1580Y</td>
<td>N1563Y</td>
<td>N1580Y</td>
<td style='text-align: right'>1757</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.9815773630343166</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2429788</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>0</td>
<td style='background-color: red'>24</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>6.2383</td>
<td>0</td>
<td>19.406</td>
<td>-0.46509</td>
<td>C</td>
<td>missense_variant</td>
<td>n.4751T>C</td>
<td>p.Ile1584Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0123456790123</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429556</td>
<td style='text-align: right'>2429801</td>
<td>30</td>
<td>I1584T</td>
<td>I1558T</td>
<td>I1558T</td>
<td>I1568T</td>
<td>I1497T</td>
<td>I1475T</td>
<td>I1530T</td>
<td>I1551T</td>
<td>I1540T</td>
<td>I1540T</td>
<td>I1594T</td>
<td>I1577T</td>
<td>I1594T</td>
<td style='text-align: right'>1758</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.110)'>
<td>2L</td>
<td>2429897</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>11</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.5234</td>
<td>1</td>
<td>16.906</td>
<td>-0.56006</td>
<td>G</td>
<td>missense_variant</td>
<td>n.4790A>G</td>
<td>p.Glu1597Gly</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0645161290323</td>
<td style='text-align: right'>0.0432098765432</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429872</td>
<td style='text-align: right'>2430142</td>
<td>31</td>
<td>E1597G</td>
<td>E1571G</td>
<td>E1571G</td>
<td>E1581G</td>
<td>E1510G</td>
<td>E1488G</td>
<td>E1543G</td>
<td>E1564G</td>
<td>E1553G</td>
<td>E1553G</td>
<td>E1607G</td>
<td>E1590G</td>
<td>E1607G</td>
<td style='text-align: right'>1761</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.070)'>
<td>2L</td>
<td>2429915</td>
<td>2</td>
<td>A</td>
<td>C</td>
<td>7</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>13</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.2461</td>
<td>0</td>
<td>16.406</td>
<td>-1.6729</td>
<td>C</td>
<td>missense_variant</td>
<td>n.4808A>C</td>
<td>p.Lys1603Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0507246376812</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429872</td>
<td style='text-align: right'>2430142</td>
<td>31</td>
<td>K1603T</td>
<td>K1577T</td>
<td>K1577T</td>
<td>K1587T</td>
<td>K1516T</td>
<td>K1494T</td>
<td>K1549T</td>
<td>K1570T</td>
<td>K1559T</td>
<td>K1559T</td>
<td>K1613T</td>
<td>K1596T</td>
<td>K1613T</td>
<td style='text-align: right'>1762</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2429958</td>
<td>2</td>
<td>A</td>
<td>C</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.0488</td>
<td>0</td>
<td>12.539</td>
<td>-1.8672</td>
<td>C</td>
<td>missense_variant</td>
<td>n.4851A>C</td>
<td>p.Leu1617Phe</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429872</td>
<td style='text-align: right'>2430142</td>
<td>31</td>
<td>L1617F</td>
<td>L1591F</td>
<td>L1591F</td>
<td>L1601F</td>
<td>L1530F</td>
<td>L1508F</td>
<td>L1563F</td>
<td>L1584F</td>
<td>L1573F</td>
<td>L1573F</td>
<td>L1627F</td>
<td>L1610F</td>
<td>L1627F</td>
<td style='text-align: right'>1763</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.030)'>
<td>2L</td>
<td>2430106</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>3</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>0</td>
<td style='background-color: red'>18</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.6719</td>
<td>0</td>
<td>15.719</td>
<td>-1.3877</td>
<td>A</td>
<td>missense_variant</td>
<td>n.4999T>A</td>
<td>p.Leu1667Met</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0217391304348</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2429872</td>
<td style='text-align: right'>2430142</td>
<td>31</td>
<td>L1667M</td>
<td>L1641M</td>
<td>L1641M</td>
<td>L1651M</td>
<td>L1580M</td>
<td>L1558M</td>
<td>L1613M</td>
<td>L1634M</td>
<td>L1623M</td>
<td>L1623M</td>
<td>L1677M</td>
<td>L1660M</td>
<td>L1677M</td>
<td style='text-align: right'>1764</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.040)'>
<td>2L</td>
<td>2430229</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>4</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>1</td>
<td style='background-color: red'>18</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.531</td>
<td>0</td>
<td>14.383</td>
<td>0.22498</td>
<td>A</td>
<td>missense_variant</td>
<td>n.5041G>A</td>
<td>p.Val1681Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00727272727273</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430224</td>
<td style='text-align: right'>2430528</td>
<td>32</td>
<td>V1681I</td>
<td>V1655I</td>
<td>V1655I</td>
<td>V1665I</td>
<td>V1594I</td>
<td>V1572I</td>
<td>V1627I</td>
<td>V1648I</td>
<td>V1637I</td>
<td>V1637I</td>
<td>V1691I</td>
<td>V1674I</td>
<td>V1691I</td>
<td style='text-align: right'>1766</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.070)'>
<td>2L</td>
<td>2430236</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>7</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td>0</td>
<td>1</td>
<td style='background-color: red'>17</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.0479</td>
<td>1</td>
<td>14.352</td>
<td>-0.62988</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5048G>T</td>
<td>p.Ser1683Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0127272727273</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430224</td>
<td style='text-align: right'>2430528</td>
<td>32</td>
<td>S1683I</td>
<td>S1657I</td>
<td>S1657I</td>
<td>S1667I</td>
<td>S1596I</td>
<td>S1574I</td>
<td>S1629I</td>
<td>S1650I</td>
<td>S1639I</td>
<td>S1639I</td>
<td>S1693I</td>
<td>S1676I</td>
<td>S1693I</td>
<td style='text-align: right'>1767</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.280)'>
<td>2L</td>
<td>2430424</td>
<td>2</td>
<td>G</td>
<td>T</td>
<td>28</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.4297</td>
<td>3</td>
<td>17.094</td>
<td>-0.71924</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5236G>T</td>
<td>p.Ala1746Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.112903225806</td>
<td style='text-align: right'>0.12962962963</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430224</td>
<td style='text-align: right'>2430528</td>
<td>32</td>
<td>A1746S</td>
<td>A1720S</td>
<td>A1720S</td>
<td>A1730S</td>
<td>A1659S</td>
<td>A1637S</td>
<td>A1692S</td>
<td>A1713S</td>
<td>A1702S</td>
<td>A1702S</td>
<td>A1756S</td>
<td>A1739S</td>
<td>A1756S</td>
<td style='text-align: right'>1772</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2430451</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.56689</td>
<td>0</td>
<td>16.047</td>
<td>0.098022</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5263C>T</td>
<td>p.His1755Tyr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00892857142857</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430224</td>
<td style='text-align: right'>2430528</td>
<td>32</td>
<td>H1755Y</td>
<td>H1729Y</td>
<td>H1729Y</td>
<td>H1739Y</td>
<td>H1668Y</td>
<td>H1646Y</td>
<td>H1701Y</td>
<td>H1722Y</td>
<td>H1711Y</td>
<td>H1711Y</td>
<td>H1765Y</td>
<td>H1748Y</td>
<td>H1765Y</td>
<td style='text-align: right'>1773</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.130)'>
<td>2L</td>
<td>2430817</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>13</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.3701</td>
<td>0</td>
<td>14.648</td>
<td>-0.66504</td>
<td>A</td>
<td>missense_variant</td>
<td>n.5557G>A</td>
<td>p.Val1853Ile</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0806451612903</td>
<td style='text-align: right'>0.0493827160494</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>V1853I</td>
<td>V1827I</td>
<td>V1827I</td>
<td>V1837I</td>
<td>V1766I</td>
<td>V1744I</td>
<td>V1799I</td>
<td>V1820I</td>
<td>V1809I</td>
<td>V1809I</td>
<td>V1863I</td>
<td>V1846I</td>
<td>V1863I</td>
<td style='text-align: right'>1778</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.520)'>
<td>2L</td>
<td>2430863</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>52</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.4785</td>
<td>0</td>
<td>15.812</td>
<td>0.78809</td>
<td>C</td>
<td>missense_variant</td>
<td>n.5603T>C</td>
<td>p.Ile1868Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.177419354839</td>
<td style='text-align: right'>0.253086419753</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>I1868T</td>
<td>I1842T</td>
<td>I1842T</td>
<td>I1852T</td>
<td>I1781T</td>
<td>I1759T</td>
<td>I1814T</td>
<td>I1835T</td>
<td>I1824T</td>
<td>I1824T</td>
<td>I1878T</td>
<td>I1861T</td>
<td>I1878T</td>
<td style='text-align: right'>1780</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.290)'>
<td>2L</td>
<td>2430880</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>29</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>19.312</td>
<td>1</td>
<td>16.547</td>
<td>-1.8408</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5620C>T</td>
<td>p.Pro1874Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.210144927536</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>P1874S</td>
<td>P1848S</td>
<td>P1848S</td>
<td>P1858S</td>
<td>P1787S</td>
<td>P1765S</td>
<td>P1820S</td>
<td>P1841S</td>
<td>P1830S</td>
<td>P1830S</td>
<td>P1884S</td>
<td>P1867S</td>
<td>P1884S</td>
<td style='text-align: right'>1781</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.800)'>
<td>2L</td>
<td>2430881</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>80</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4453</td>
<td>1</td>
<td>18.562</td>
<td>-1.4189</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5621C>T</td>
<td>p.Pro1874Leu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0724637681159</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.451612903226</td>
<td style='text-align: right'>0.259259259259</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>P1874L</td>
<td>P1848L</td>
<td>P1848L</td>
<td>P1858L</td>
<td>P1787L</td>
<td>P1765L</td>
<td>P1820L</td>
<td>P1841L</td>
<td>P1830L</td>
<td>P1830L</td>
<td>P1884L</td>
<td>P1867L</td>
<td>P1884L</td>
<td style='text-align: right'>1782</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.120)'>
<td>2L</td>
<td>2431019</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>12</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.85107</td>
<td>1</td>
<td>13.523</td>
<td>-1.6211</td>
<td>C</td>
<td>missense_variant</td>
<td>n.5759T>C</td>
<td>p.Phe1920Ser</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0145454545455</td>
<td style='text-align: right'>0.0357142857143</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>F1920S</td>
<td>F1894S</td>
<td>F1894S</td>
<td>F1904S</td>
<td>F1833S</td>
<td>F1811S</td>
<td>F1866S</td>
<td>F1887S</td>
<td>F1876S</td>
<td>F1876S</td>
<td>F1930S</td>
<td>F1913S</td>
<td>F1930S</td>
<td style='text-align: right'>1786</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.160)'>
<td>2L</td>
<td>2431061</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>16</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>8</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.5</td>
<td>1</td>
<td>16.688</td>
<td>-0.46802</td>
<td>T</td>
<td>missense_variant</td>
<td>n.5801C>T</td>
<td>p.Ala1934Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.115942028986</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>A1934V</td>
<td>A1908V</td>
<td>A1908V</td>
<td>A1918V</td>
<td>A1847V</td>
<td>A1825V</td>
<td>A1880V</td>
<td>A1901V</td>
<td>A1890V</td>
<td>A1890V</td>
<td>A1944V</td>
<td>A1927V</td>
<td>A1944V</td>
<td style='text-align: right'>1787</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.440)'>
<td>2L</td>
<td>2431079</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>44</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.4004</td>
<td>0</td>
<td>15.953</td>
<td>2.1738</td>
<td>C</td>
<td>missense_variant</td>
<td>n.5819T>C</td>
<td>p.Ile1940Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0434782608696</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0690909090909</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>I1940T</td>
<td>I1914T</td>
<td>I1914T</td>
<td>I1924T</td>
<td>I1853T</td>
<td>I1831T</td>
<td>I1886T</td>
<td>I1907T</td>
<td>I1896T</td>
<td>I1896T</td>
<td>I1950T</td>
<td>I1933T</td>
<td>I1950T</td>
<td style='text-align: right'>1788</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2431232</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.1719</td>
<td>2</td>
<td>12.328</td>
<td>-0.80713</td>
<td>A</td>
<td>missense_variant</td>
<td>n.5972G>A</td>
<td>p.Gly1991Glu</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>G1991E</td>
<td>G1965E</td>
<td>G1965E</td>
<td>G1975E</td>
<td>G1904E</td>
<td>G1882E</td>
<td>G1937E</td>
<td>G1958E</td>
<td>G1947E</td>
<td>G1947E</td>
<td>G2001E</td>
<td>G1984E</td>
<td>G2001E</td>
<td style='text-align: right'>1791</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2431331</td>
<td>2</td>
<td>C</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>4.1406</td>
<td>2</td>
<td>12.797</td>
<td>-0.031006</td>
<td>A</td>
<td>missense_variant</td>
<td>n.6071C>A</td>
<td>p.Thr2024Lys</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>T2024K</td>
<td>T1998K</td>
<td>T1998K</td>
<td>T2008K</td>
<td>T1937K</td>
<td>T1915K</td>
<td>T1970K</td>
<td>T1991K</td>
<td>T1980K</td>
<td>T1980K</td>
<td>T2034K</td>
<td>T2017K</td>
<td>T2034K</td>
<td style='text-align: right'>1793</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2431417</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>5</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>10.93</td>
<td>0</td>
<td>13.789</td>
<td>-1.9297</td>
<td>G</td>
<td>missense_variant</td>
<td>n.6157A>G</td>
<td>p.Ile2053Val</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00363636363636</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>I2053V</td>
<td>I2027V</td>
<td>I2027V</td>
<td>I2037V</td>
<td>I1966V</td>
<td>I1944V</td>
<td>I1999V</td>
<td>I2020V</td>
<td>I2009V</td>
<td>I2009V</td>
<td>I2063V</td>
<td>I2046V</td>
<td>I2063V</td>
<td style='text-align: right'>1796</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.050)'>
<td>2L</td>
<td>2431487</td>
<td>2</td>
<td>G</td>
<td>C</td>
<td>5</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>6</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.69678</td>
<td>1</td>
<td>14.32</td>
<td>-0.78418</td>
<td>C</td>
<td>missense_variant</td>
<td>n.6227G>C</td>
<td>p.Ser2076Thr</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00909090909091</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2430601</td>
<td style='text-align: right'>2431617</td>
<td>33</td>
<td>S2076T</td>
<td>S2050T</td>
<td>S2050T</td>
<td>S2060T</td>
<td>S1989T</td>
<td>S1967T</td>
<td>S2022T</td>
<td>S2043T</td>
<td>S2032T</td>
<td>S2032T</td>
<td>S2086T</td>
<td>S2069T</td>
<td>S2086T</td>
<td style='text-align: right'>1797</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>



## Inspect splice site variants


```python
def simplify_intron_effect(v):
    if v and v[0] in ['SPLICE_REGION', 'SPLICE_CORE']:
        if math.fabs(v[2]) < math.fabs(v[4]):
            return v[1], v[2]
        else:
            return v[3], v[4]
    else:
        return ''

    
td_styles = {
    'FILTER_PASS': lambda v: 'background-color: red' if not v else '',
    'NoCoverage': lambda v: 'background-color: red' if v > 1 else '',
    'LowCoverage': lambda v: 'background-color: red' if v > 76 else '',
    'HighCoverage': lambda v: 'background-color: red' if v > 15 else '',
    'LowMQ': lambda v: 'background-color: red' if v > 76 else '',
    'HighMQ0': lambda v: 'background-color: red' if v > 1 else '',
    'RepeatDUST': lambda v: 'background-color: red' if v else '',
    'FS': lambda v: 'background-color: red' if v > 60 else '',
    'QD': lambda v: 'background-color: red' if v < 5 else '',
    'ReadPosRankSum': lambda v: 'background-color: red' if v < -8 else '',
    'HRun': lambda v: 'background-color: red' if v > 4 else '',
    'num_alleles': lambda v: 'background-color: orange' if v > 2 else '',
}


def tr_style(row):
    """Colour row by alternate allele count."""
    return 'background-color:rgba(0, 255, 0, %.3f)' % (min(1, row['AC']/100))


tbl_variants_phase1_splice = (
    tbl_variants_phase1_eff_ld
    .select(lambda row: any(row[t] and row[t][0] in ['SPLICE_REGION', 'SPLICE_CORE'] for t in transcript_ids))
    .convert(transcript_ids, simplify_intron_effect)
)
tbl_variants_phase1_splice.displayall(td_styles=td_styles, tr_style=tr_style)
```


<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
<th>51|haps_vidx</th>
<th>52|dprime_L995S</th>
<th>53|dprime_L995F</th>
</tr>
</thead>
<tbody>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2362002</td>
<td>2</td>
<td>A</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.5459</td>
<td>0</td>
<td>12.531</td>
<td>-0.55322</td>
<td>T</td>
<td>splice_region_variant&intron_varia</td>
<td>n.148-5A>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
<td>('AGAP004707-PA', -5)</td>
<td>('AGAP004707-PB', -5)</td>
<td>('AGAP004707-PC', -5)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td style='text-align: right'>223</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2362003</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>3</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.50195</td>
<td>0</td>
<td>14.062</td>
<td>0.024994</td>
<td>T</td>
<td>splice_region_variant&intron_varia</td>
<td>n.148-4C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0144927536232</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2361989</td>
<td style='text-align: right'>2362144</td>
<td>3</td>
<td>('AGAP004707-PA', -4)</td>
<td>('AGAP004707-PB', -4)</td>
<td>('AGAP004707-PC', -4)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td style='text-align: right'>224</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2382263</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>166</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>45</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.957</td>
<td>0</td>
<td>25.375</td>
<td>-2.8809</td>
<td>G</td>
<td>splice_region_variant&intron_varia</td>
<td>n.492-7A>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.00833333333333</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.47572815534</td>
<td style='text-align: right'>0.761363636364</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', -7)</td>
<td>('AGAP004707-PB', -7)</td>
<td>('AGAP004707-PC', -7)</td>
<td>('5', -7)</td>
<td></td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td>('5', -7)</td>
<td style='text-align: right'>575</td>
<td style='text-align: right'>0.9916210295728368</td>
<td style='text-align: right'>-0.9881072677808006</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2390126</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>11</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>3.4746</td>
<td>0</td>
<td>14.32</td>
<td>-1.0264</td>
<td>T</td>
<td>splice_region_variant&intron_varia</td>
<td>n.713-3C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00363636363636</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', -3)</td>
<td>('AGAP004707-PB', -3)</td>
<td>('AGAP004707-PC', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td>('7', -3)</td>
<td style='text-align: right'>896</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.010)'>
<td>2L</td>
<td>2400176</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>0.0</td>
<td>0</td>
<td>22.203</td>
<td>0.74316</td>
<td>G</td>
<td>splice_region_variant&intron_varia</td>
<td>n.1572+3A>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', 3)</td>
<td>('AGAP004707-PB', 3)</td>
<td>('AGAP004707-PC', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td>('11i+', 3)</td>
<td style='text-align: right'>1166</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.040)'>
<td>2L</td>
<td>2407888</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>4</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>2</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>5.7578</td>
<td>0</td>
<td>16.281</td>
<td>-0.76416</td>
<td>C</td>
<td>splice_region_variant&intron_varia</td>
<td>n.2017-6T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0434782608696</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', -6)</td>
<td>('AGAP004707-PB', -6)</td>
<td>('AGAP004707-PC', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td>('16', -6)</td>
<td style='text-align: right'>1298</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 1.000)'>
<td>2L</td>
<td>2417362</td>
<td>2</td>
<td>A</td>
<td>G</td>
<td>496</td>
<td style='text-align: right'>0</td>
<td style='background-color: red'>False</td>
<td style='background-color: red'>5</td>
<td style='background-color: red'>712</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td style='background-color: red'>63.062</td>
<td>1</td>
<td>28.844</td>
<td>1.251</td>
<td>G</td>
<td>splice_region_variant&intron_varia</td>
<td>n.2637+4A>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.838983050847</td>
<td style='text-align: right'>0.840579710145</td>
<td style='text-align: right'>0.0666666666667</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>0.0967153284672</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', 4)</td>
<td>('AGAP004707-PB', 4)</td>
<td>('AGAP004707-PC', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>('19', 4)</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.790)'>
<td>2L</td>
<td>2425766</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>79</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>9</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.9062</td>
<td>0</td>
<td>21.391</td>
<td>1.6143</td>
<td>A</td>
<td>intron_variant</td>
<td>n.4068+315T></td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0145454545455</td>
<td style='text-align: right'>0.633928571429</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>('27k', -4)</td>
<td style='text-align: right'>1680</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color:rgba(0, 255, 0, 0.020)'>
<td>2L</td>
<td>2429868</td>
<td>2</td>
<td>C</td>
<td>A</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>8.5469</td>
<td>0</td>
<td>14.961</td>
<td>-0.014</td>
<td>A</td>
<td>splice_region_variant&intron_varia</td>
<td>n.4765-4C>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0217391304348</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('AGAP004707-PA', -4)</td>
<td>('AGAP004707-PB', -4)</td>
<td>('AGAP004707-PC', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td>('31', -4)</td>
<td style='text-align: right'>1759</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>



## Write out variants to file


```python
(tbl_variants_phase1_eff_ld
 .teepickle('../data/tbl_variants_phase1.pkl')
 .convert(transcript_ids, lambda v: ':'.join(map(str, v)))
 .replaceall(None, 'NA')
 .totsv('../data/tbl_variants_phase1.txt')
)
```


```python
# check OK
etl.frompickle('../data/tbl_variants_phase1.pkl')
```




<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
<th>51|haps_vidx</th>
<th>52|dprime_L995S</th>
<th>53|dprime_L995F</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00181818181818</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td style='text-align: right'>2358158</td>
<td style='text-align: right'>2358304</td>
<td>1</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td>('NON_SYNONYMOUS_CODING', 'D33N')</td>
<td style='text-align: right'>83</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358316</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>73</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4844</td>
<td>0</td>
<td>16.438</td>
<td>1.4219</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+12T>G</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.132727272727</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 12, 'AGAP004707-PA', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PB', 12, 'AGAP004707-PB', -3691)</td>
<td>('INTRONIC', 'AGAP004707-PC', 12, 'AGAP004707-PC', -3691)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td>('INTRONIC', '1', 12, '2j', -1324)</td>
<td>('INTRONIC', '1', 12, '3', -3673)</td>
<td style='text-align: right'>84</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358328</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.7363</td>
<td>0</td>
<td>16.062</td>
<td>-0.646</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+24T>C</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.00724637681159</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 24, 'AGAP004707-PA', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PB', 24, 'AGAP004707-PB', -3679)</td>
<td>('INTRONIC', 'AGAP004707-PC', 24, 'AGAP004707-PC', -3679)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td>('INTRONIC', '1', 24, '2j', -1312)</td>
<td>('INTRONIC', '1', 24, '3', -3661)</td>
<td style='text-align: right'>85</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358353</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9512</td>
<td>0</td>
<td>9.8594</td>
<td>1.1582</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+49C>T</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 49, 'AGAP004707-PA', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PB', 49, 'AGAP004707-PB', -3654)</td>
<td>('INTRONIC', 'AGAP004707-PC', 49, 'AGAP004707-PC', -3654)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td>('INTRONIC', '1', 49, '2j', -1287)</td>
<td>('INTRONIC', '1', 49, '3', -3636)</td>
<td style='text-align: right'>86</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358405</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>1</td>
<td style='text-align: right'>0</td>
<td>True</td>
<td>0</td>
<td>6</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.844</td>
<td>1</td>
<td>10.859</td>
<td>1.1562</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+101T>A</td>
<td>None</td>
<td>AGAP004707-RA</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0108695652174</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td style='text-align: right'>0.0</td>
<td>True</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>('INTRONIC', 'AGAP004707-PA', 101, 'AGAP004707-PA', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PB', 101, 'AGAP004707-PB', -3602)</td>
<td>('INTRONIC', 'AGAP004707-PC', 101, 'AGAP004707-PC', -3602)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td>('INTRONIC', '1', 101, '2j', -1235)</td>
<td>('INTRONIC', '1', 101, '3', -3584)</td>
<td style='text-align: right'>87</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>




```python
etl.fromtsv('../data/tbl_variants_phase1.txt')
```




<table class='petl'>
<thead>
<tr>
<th>0|CHROM</th>
<th>1|POS</th>
<th>2|num_alleles</th>
<th>3|REF</th>
<th>4|ALT</th>
<th>5|AC</th>
<th>6|ALTIX</th>
<th>7|FILTER_PASS</th>
<th>8|NoCoverage</th>
<th>9|LowCoverage</th>
<th>10|HighCoverage</th>
<th>11|LowMQ</th>
<th>12|HighMQ0</th>
<th>13|RepeatDUST</th>
<th>14|RepeatMasker</th>
<th>15|RepeatTRF</th>
<th>16|FS</th>
<th>17|HRun</th>
<th>18|QD</th>
<th>19|ReadPosRankSum</th>
<th>20|SNPEFF_Allele</th>
<th>21|SNPEFF_Annotation</th>
<th>22|SNPEFF_HGVS_c</th>
<th>23|SNPEFF_HGVS_p</th>
<th>24|SNPEFF_Feature_ID</th>
<th>25|AF_AOM</th>
<th>26|AF_BFM</th>
<th>27|AF_GWA</th>
<th>28|AF_GNS</th>
<th>29|AF_BFS</th>
<th>30|AF_CMS</th>
<th>31|AF_GAS</th>
<th>32|AF_UGS</th>
<th>33|AF_KES</th>
<th>34|check_allele</th>
<th>35|exon_start</th>
<th>36|exon_end</th>
<th>37|exon</th>
<th>38|AGAP004707-RA</th>
<th>39|AGAP004707-RB</th>
<th>40|AGAP004707-RC</th>
<th>41|Davies-C1N2</th>
<th>42|Davies-C3N2</th>
<th>43|Davies-C5N2</th>
<th>44|Davies-C7N2</th>
<th>45|Davies-C8N2</th>
<th>46|Davies-C10N2</th>
<th>47|Davies-C11N2</th>
<th>48|Davies-C1N9</th>
<th>49|Davies-C8N9</th>
<th>50|Davies-C1N9ck</th>
<th>51|haps_vidx</th>
<th>52|dprime_L995S</th>
<th>53|dprime_L995F</th>
</tr>
</thead>
<tbody>
<tr>
<td>2L</td>
<td>2358254</td>
<td>2</td>
<td>G</td>
<td>A</td>
<td>1</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>10</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>9.8672</td>
<td>1</td>
<td>17.547</td>
<td>-0.049988</td>
<td>A</td>
<td>missense_variant</td>
<td>n.97G>A</td>
<td>p.Asp33Asn</td>
<td>AGAP004707-RA</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00181818181818</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>True</td>
<td>2358158</td>
<td>2358304</td>
<td>1</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>NON_SYNONYMOUS_CODING:D33N</td>
<td>83</td>
<td>-1.0</td>
<td>1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358316</td>
<td>2</td>
<td>T</td>
<td>G</td>
<td>73</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.4844</td>
<td>0</td>
<td>16.438</td>
<td>1.4219</td>
<td>G</td>
<td>intron_variant</td>
<td>n.147+12T>G</td>
<td>NA</td>
<td>AGAP004707-RA</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.132727272727</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>True</td>
<td>NA</td>
<td>NA</td>
<td>NA</td>
<td>INTRONIC:AGAP004707-PA:12:AGAP004707-PA:-3691</td>
<td>INTRONIC:AGAP004707-PB:12:AGAP004707-PB:-3691</td>
<td>INTRONIC:AGAP004707-PC:12:AGAP004707-PC:-3691</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:2j:-1324</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>INTRONIC:1:12:2j:-1324</td>
<td>INTRONIC:1:12:3:-3673</td>
<td>84</td>
<td>1.0</td>
<td>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358328</td>
<td>2</td>
<td>T</td>
<td>C</td>
<td>2</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>0</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>2.7363</td>
<td>0</td>
<td>16.062</td>
<td>-0.646</td>
<td>C</td>
<td>intron_variant</td>
<td>n.147+24T>C</td>
<td>NA</td>
<td>AGAP004707-RA</td>
<td>0.0</td>
<td>0.00724637681159</td>
<td>0.0108695652174</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>True</td>
<td>NA</td>
<td>NA</td>
<td>NA</td>
<td>INTRONIC:AGAP004707-PA:24:AGAP004707-PA:-3679</td>
<td>INTRONIC:AGAP004707-PB:24:AGAP004707-PB:-3679</td>
<td>INTRONIC:AGAP004707-PC:24:AGAP004707-PC:-3679</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:2j:-1312</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>INTRONIC:1:24:2j:-1312</td>
<td>INTRONIC:1:24:3:-3661</td>
<td>85</td>
<td>-1.0</td>
<td>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358353</td>
<td>2</td>
<td>C</td>
<td>T</td>
<td>1</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>1</td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>1.9512</td>
<td>0</td>
<td>9.8594</td>
<td>1.1582</td>
<td>T</td>
<td>intron_variant</td>
<td>n.147+49C>T</td>
<td>NA</td>
<td>AGAP004707-RA</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0108695652174</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>True</td>
<td>NA</td>
<td>NA</td>
<td>NA</td>
<td>INTRONIC:AGAP004707-PA:49:AGAP004707-PA:-3654</td>
<td>INTRONIC:AGAP004707-PB:49:AGAP004707-PB:-3654</td>
<td>INTRONIC:AGAP004707-PC:49:AGAP004707-PC:-3654</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:2j:-1287</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>INTRONIC:1:49:2j:-1287</td>
<td>INTRONIC:1:49:3:-3636</td>
<td>86</td>
<td>-1.0</td>
<td>-1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2358405</td>
<td>2</td>
<td>T</td>
<td>A</td>
<td>1</td>
<td>0</td>
<td>True</td>
<td>0</td>
<td>6</td>
<td>14</td>
<td>0</td>
<td>0</td>
<td>False</td>
<td>False</td>
<td>False</td>
<td>20.844</td>
<td>1</td>
<td>10.859</td>
<td>1.1562</td>
<td>A</td>
<td>intron_variant</td>
<td>n.147+101T>A</td>
<td>NA</td>
<td>AGAP004707-RA</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0108695652174</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>True</td>
<td>NA</td>
<td>NA</td>
<td>NA</td>
<td>INTRONIC:AGAP004707-PA:101:AGAP004707-PA:-3602</td>
<td>INTRONIC:AGAP004707-PB:101:AGAP004707-PB:-3602</td>
<td>INTRONIC:AGAP004707-PC:101:AGAP004707-PC:-3602</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:2j:-1235</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>INTRONIC:1:101:2j:-1235</td>
<td>INTRONIC:1:101:3:-3584</td>
<td>87</td>
<td>-1.0</td>
<td>-1.0</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>




```python

```
