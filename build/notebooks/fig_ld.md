

```python
%run setup.ipynb
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
%matplotlib inline
```


```python
tbl_variants = etl.frompickle('../data/tbl_variants_phase1.pkl')
tbl_variants.head()
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
<td style='text-align: right'>0</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
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
<td style='text-align: right'>1</td>
<td style='text-align: right'>0.9809464508094645</td>
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
<td style='text-align: right'>2</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.012903225806451613</td>
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
<td style='text-align: right'>3</td>
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
<td style='text-align: right'>4</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>





```python
transcript_ids = [
    'AGAP004707-RA',
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
    'Davies-C1N9ck'
]
```


```python
pop_ids = 'AOM BFM GWA GNS BFS CMS GAS UGS KES'.split()
```


```python
# keep only the missense variants


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
for p in pop_ids:
    td_styles['AF_' + p] = lambda v: 'background-color: blue' if v > .05 else ''



def tr_style(row):
    """Colour row by alternate allele count."""
    return 'background-color: green' if row['AC'] > 14 else ''


tbl_variants_missense = (
    tbl_variants
    .select(lambda row: any(row[t] and row[t][0] == 'NON_SYNONYMOUS_CODING' for t in transcript_ids))
    .convert(transcript_ids, simplify_missense_effect)

)
tbl_variants_missense.displayall(tr_style=tr_style, td_styles=td_styles)
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
<td style='text-align: right'>0</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0109090909091</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0113636363636</td>
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
<tr>
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
<td>0.0</td>
<td>0.0144927536232</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>140</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0144927536232</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>142</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00617283950617</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>143</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0178571428571</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>816</td>
<td style='text-align: right'>0.30454545454545456</td>
<td style='text-align: right'>-0.012903225806451613</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.316363636364</td>
<td style='background-color: blue'>0.214285714286</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>817</td>
<td style='text-align: right'>-0.9640591966173362</td>
<td style='text-align: right'>0.9181216134858519</td>
</tr>
<tr>
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
<td style='text-align: right'>821</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0109090909091</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>828</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0724637681159</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.8025806451612904</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0652173913043</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0690909090909</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1080</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.181818181818</td>
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
<td style='text-align: right'>1083</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00363636363636</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1083</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00970873786408</td>
<td>0.0</td>
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
<td style='text-align: right'>1084</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00892857142857</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1136</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00617283950617</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1137</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td style='text-align: right'>1213</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1217</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.00724637681159</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1218</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<tr>
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
<td>0.00833333333333</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0144927536232</td>
<td>0.0</td>
<td style='background-color: blue'>0.129032258065</td>
<td style='background-color: blue'>0.135802469136</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1434</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1448</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1449</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00485436893204</td>
<td>0.0</td>
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
<td style='text-align: right'>1455</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.00724637681159</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1516</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00617283950617</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1529</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.154545454545</td>
<td style='background-color: blue'>0.642857142857</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>0.761363636364</td>
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
<td style='text-align: right'>1531</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td style='background-color: blue'>0.858333333333</td>
<td style='background-color: blue'>0.847826086957</td>
<td>0.0</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>0.529090909091</td>
<td style='background-color: blue'>0.357142857143</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1532</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td style='text-align: right'>1564</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td style='background-color: blue'>0.0916666666667</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1565</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.46158357771261</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00181818181818</td>
<td>0.00892857142857</td>
<td>0.0</td>
<td>0.0</td>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td>0.00833333333333</td>
<td>0.0144927536232</td>
<td>0.0108695652174</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0109090909091</td>
<td>0.00892857142857</td>
<td>0.0</td>
<td>0.0</td>
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
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.054347826087</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1580</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00617283950617</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1584</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0217391304348</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1585</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00617283950617</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1645</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.13768115942</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1671</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.8960950764006791</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00485436893204</td>
<td>0.0</td>
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
<td style='text-align: right'>1672</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.260869565217</td>
<td>0.0</td>
<td style='background-color: blue'>0.0967741935484</td>
<td style='background-color: blue'>0.216049382716</td>
<td style='background-color: blue'>0.06</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1673</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.9815773630343166</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0123456790123</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0645161290323</td>
<td>0.0432098765432</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1676</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0507246376812</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1677</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1678</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0217391304348</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00727272727273</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0127272727273</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.112903225806</td>
<td style='background-color: blue'>0.12962962963</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1684</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00892857142857</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1685</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0806451612903</td>
<td>0.0493827160494</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1690</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.177419354839</td>
<td style='background-color: blue'>0.253086419753</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1692</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.210144927536</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1693</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.0724637681159</td>
<td>0.0</td>
<td style='background-color: blue'>0.451612903226</td>
<td style='background-color: blue'>0.259259259259</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1694</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.9746688741721854</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0145454545455</td>
<td>0.0357142857143</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1698</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.115942028986</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1699</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0434782608696</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0690909090909</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1700</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1703</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1705</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00363636363636</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1708</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00909090909091</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1709</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>




```python
# select only variants above 5% frequency in one or more populations, except
# for some manual overrides

manual_overrides = [
    2400071,
    2431019
]

tbl_variants_selected = (
    tbl_variants_missense
    .select(lambda row: any(row['AF_' + p] > 0.05 for p in pop_ids) or row['POS'] in manual_overrides)
)
tbl_variants_selected.displayall(tr_style=tr_style, td_styles=td_styles)
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
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.316363636364</td>
<td style='background-color: blue'>0.214285714286</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>817</td>
<td style='text-align: right'>-0.9640591966173362</td>
<td style='text-align: right'>0.9181216134858519</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0724637681159</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.8025806451612904</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0652173913043</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0690909090909</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1080</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.181818181818</td>
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
<td style='text-align: right'>1083</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.00363636363636</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1083</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0144927536232</td>
<td>0.0</td>
<td style='background-color: blue'>0.129032258065</td>
<td style='background-color: blue'>0.135802469136</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1434</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.154545454545</td>
<td style='background-color: blue'>0.642857142857</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>0.761363636364</td>
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
<td style='text-align: right'>1531</td>
<td style='text-align: right'>1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td style='background-color: blue'>0.858333333333</td>
<td style='background-color: blue'>0.847826086957</td>
<td>0.0</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>1.0</td>
<td style='background-color: blue'>0.529090909091</td>
<td style='background-color: blue'>0.357142857143</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1532</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td style='background-color: blue'>0.0916666666667</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1565</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.46158357771261</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.054347826087</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1580</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.13768115942</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1671</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.8960950764006791</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.260869565217</td>
<td>0.0</td>
<td style='background-color: blue'>0.0967741935484</td>
<td style='background-color: blue'>0.216049382716</td>
<td style='background-color: blue'>0.06</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1673</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.9815773630343166</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0645161290323</td>
<td>0.0432098765432</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1676</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td style='background-color: blue'>0.0507246376812</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1677</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.112903225806</td>
<td style='background-color: blue'>0.12962962963</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1684</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0806451612903</td>
<td>0.0493827160494</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1690</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.177419354839</td>
<td style='background-color: blue'>0.253086419753</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1692</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.210144927536</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1693</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.0724637681159</td>
<td>0.0</td>
<td style='background-color: blue'>0.451612903226</td>
<td style='background-color: blue'>0.259259259259</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1694</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>0.9746688741721854</td>
</tr>
<tr>
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
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0145454545455</td>
<td>0.0357142857143</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1698</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td style='background-color: blue'>0.115942028986</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1699</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr style='background-color: green'>
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
<td>0.0</td>
<td>0.0434782608696</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
<td style='background-color: blue'>0.0690909090909</td>
<td>0.0</td>
<td>0.0</td>
<td>0.0</td>
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
<td style='text-align: right'>1700</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
</tbody>
</table>




```python
tbl_variants_selected.nrows()
```




    23




```python
region_vgsc = SeqFeature('2L', 2358158, 2431617)
# these are the biallelics phased with shapeit2
callset_phased = phase1_ar31.callset_phased
# positions of all biallelic SNPs in the shapeit2 callset
pos_biallelic = allel.SortedIndex(callset_phased['2L/variants/POS'])
```


```python
# extract to region
loc_vgsc_region = pos_biallelic.locate_range(region_vgsc.start, region_vgsc.end)
pos_biallelic_vgsc = pos_biallelic[loc_vgsc_region]
haps_biallelic_vgsc = allel.GenotypeArray(callset_phased['2L/calldata/genotype'][loc_vgsc_region, :765]).to_haplotypes()
pos_biallelic_vgsc
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(1710,) dtype=int32&gt;</span><table><thead><tr><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1705</th><th style="text-align: center">1706</th><th style="text-align: center">1707</th><th style="text-align: center">1708</th><th style="text-align: center">1709</th></tr></thead><tbody><tr><td style="text-align: center">2358254</td><td style="text-align: center">2358316</td><td style="text-align: center">2358328</td><td style="text-align: center">2358353</td><td style="text-align: center">2358405</td><td style="text-align: center">...</td><td style="text-align: center">2431417</td><td style="text-align: center">2431487</td><td style="text-align: center">2431518</td><td style="text-align: center">2431527</td><td style="text-align: center">2431542</td></tr></tbody></table></div>




```python
haps_biallelic_vgsc
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(1710, 1530) dtype=int8&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1707</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1708</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1709</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></tbody></table></div>




```python
# these are the multiallelics phased with mvncall
callset_vgsc_phased_extras = np.load('../data/phasing_extra_phase1.mvncall.200.npz')
# positions of multiallelic SNPs in the mvncall callset
pos_extras = allel.SortedIndex(callset_vgsc_phased_extras['variants']['POS'])
pos_extras
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(3,) dtype=int32&gt;</span><table><thead><tr><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th></tr></thead><tbody><tr><td style="text-align: center">2391228</td><td style="text-align: center">2400071</td><td style="text-align: center">2429745</td></tr></tbody></table></div>




```python
# haplotypes at all phased extras sites
haps_extras = allel.GenotypeArray(callset_vgsc_phased_extras['calldata']['genotype']).to_haplotypes()
haps_extras
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(3, 1530) dtype=int8&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">2</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">1</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">1</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></tbody></table></div>




```python
# combine haplotypes for bi- and multi-allelic SNPs
haps_combined = haps_biallelic_vgsc.concatenate(haps_extras)
haps_combined
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(1713, 1530) dtype=int8&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1710</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">2</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1711</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1712</th><td style="text-align: center">1</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">1</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></tbody></table></div>




```python
pos_combined = np.array(list(pos_biallelic_vgsc) + list(pos_extras))
idx_sorted = np.argsort(pos_combined)
idx_sorted
```




    array([   0,    1,    2, ..., 1707, 1708, 1709])




```python
haps_combined = haps_combined.take(idx_sorted, axis=0)
pos_combined = allel.SortedIndex(pos_combined.take(idx_sorted, axis=0))
haps_combined
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(1713, 1530) dtype=int8&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1710</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1711</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1712</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></tbody></table></div>




```python
pos_combined
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(1713,) dtype=int32&gt;</span><table><thead><tr><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1708</th><th style="text-align: center">1709</th><th style="text-align: center">1710</th><th style="text-align: center">1711</th><th style="text-align: center">1712</th></tr></thead><tbody><tr><td style="text-align: center">2358254</td><td style="text-align: center">2358316</td><td style="text-align: center">2358328</td><td style="text-align: center">2358353</td><td style="text-align: center">2358405</td><td style="text-align: center">...</td><td style="text-align: center">2431417</td><td style="text-align: center">2431487</td><td style="text-align: center">2431518</td><td style="text-align: center">2431527</td><td style="text-align: center">2431542</td></tr></tbody></table></div>




```python
def lewontin_d_prime(h, i, j, a=1, b=1):
    """Compute LD between a pair of alleles.
    
    Parameters
    ----------
    h : array
        Haplotype array.
    i : int
        First variant index.
    j : int
        Second variant index.
    a : int
        First variant allele.
    b : int
        Second variant allele.
    
    Returns
    -------
    ld : float
    
    """
    
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
        
#     log('D_prime counts:', 'i', i, 'j', j, 'a', a, 'b', b, 'n', n, 'n_a', n_a, 'n_b', n_b)
        
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
    D_prime = D_ab / D_max
    
#     log('D_prime', D_prime, i, j, a, b, n, n_a, n_b, D_ab, D_max)
#     if np.isnan(D_prime):
#         log('nan')
#        log(D_prime, i, j, a, b, n, n_a, n_b, D_ab, D_max)
        
    return D_prime

```


```python
pos_selected = allel.SortedIndex(sorted(tbl_variants_selected.values('POS').set()))
pos_selected
```




<div class="allel allel-DisplayAs1D"><span>&lt;SortedIndex shape=(21,) dtype=int32&gt;</span><table><thead><tr><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">16</th><th style="text-align: center">17</th><th style="text-align: center">18</th><th style="text-align: center">19</th><th style="text-align: center">20</th></tr></thead><tbody><tr><td style="text-align: center">2390177</td><td style="text-align: center">2391228</td><td style="text-align: center">2399997</td><td style="text-align: center">2400071</td><td style="text-align: center">2416980</td><td style="text-align: center">...</td><td style="text-align: center">2430880</td><td style="text-align: center">2430881</td><td style="text-align: center">2431019</td><td style="text-align: center">2431061</td><td style="text-align: center">2431079</td></tr></tbody></table></div>




```python
tbl_variants_selected
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
<td style='text-align: right'>817</td>
<td style='text-align: right'>-0.9640591966173362</td>
<td style='text-align: right'>0.9181216134858519</td>
</tr>
<tr>
<td>2L</td>
<td>2391228</td>
<td>3</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-0.8025806451612904</td>
</tr>
<tr>
<td>2L</td>
<td>2391228</td>
<td>3</td>
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
<td style='text-align: right'>838</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
<tr>
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
<td style='text-align: right'>1080</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>1.0</td>
</tr>
<tr>
<td>2L</td>
<td>2400071</td>
<td>3</td>
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
<td style='text-align: right'>1083</td>
<td style='text-align: right'>-1.0</td>
<td style='text-align: right'>-1.0</td>
</tr>
</tbody>
</table>
<p><strong>...</strong></p>




```python
pos_selected.shape
```




    (21,)




```python
# be careful about multiallelics here?
loc_combined_selected = pos_combined.locate_keys(pos_selected)
np.count_nonzero(loc_combined_selected)
```




    21




```python
haps_selected = haps_combined[loc_combined_selected]
haps_selected
```




<div class="allel allel-DisplayAs2D"><span>&lt;HaplotypeArray shape=(21, 1530) dtype=int8&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th><th style="text-align: center">3</th><th style="text-align: center">4</th><th style="text-align: center">...</th><th style="text-align: center">1525</th><th style="text-align: center">1526</th><th style="text-align: center">1527</th><th style="text-align: center">1528</th><th style="text-align: center">1529</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">2</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">...</th><td style="text-align: center" colspan="12">...</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">18</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">19</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">1</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">20</th><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">...</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td><td style="text-align: center">0</td></tr></tbody></table></div>




```python
ac = haps_selected.count_alleles()
ac.displayall()
```


<div class="allel allel-DisplayAs2D"><span>&lt;AlleleCountsArray shape=(21, 3) dtype=int32&gt;</span><table><thead><tr><th></th><th style="text-align: center">0</th><th style="text-align: center">1</th><th style="text-align: center">2</th></tr></thead><tbody><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">0</th><td style="text-align: center">1332</td><td style="text-align: center"> 198</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">1</th><td style="text-align: center">1511</td><td style="text-align: center">  10</td><td style="text-align: center">   9</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">2</th><td style="text-align: center">1492</td><td style="text-align: center">  38</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">3</th><td style="text-align: center">1512</td><td style="text-align: center">  16</td><td style="text-align: center">   2</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">4</th><td style="text-align: center">1498</td><td style="text-align: center">  32</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">5</th><td style="text-align: center">1100</td><td style="text-align: center"> 430</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">6</th><td style="text-align: center"> 755</td><td style="text-align: center"> 775</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">7</th><td style="text-align: center">1519</td><td style="text-align: center">  11</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">8</th><td style="text-align: center">1525</td><td style="text-align: center">   5</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">9</th><td style="text-align: center">1511</td><td style="text-align: center">  19</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">10</th><td style="text-align: center">1420</td><td style="text-align: center"> 110</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">11</th><td style="text-align: center">1519</td><td style="text-align: center">  11</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">12</th><td style="text-align: center">1523</td><td style="text-align: center">   7</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">13</th><td style="text-align: center">1502</td><td style="text-align: center">  28</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">14</th><td style="text-align: center">1517</td><td style="text-align: center">  13</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">15</th><td style="text-align: center">1478</td><td style="text-align: center">  52</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">16</th><td style="text-align: center">1501</td><td style="text-align: center">  29</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">17</th><td style="text-align: center">1450</td><td style="text-align: center">  80</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">18</th><td style="text-align: center">1518</td><td style="text-align: center">  12</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">19</th><td style="text-align: center">1514</td><td style="text-align: center">  16</td><td style="text-align: center">   0</td></tr><tr><th style="text-align: center; background-color: white; border-right: 1px solid black; ">20</th><td style="text-align: center">1486</td><td style="text-align: center">  44</td><td style="text-align: center">   0</td></tr></tbody></table></div>



```python
tbl_variants_selected.records()[0].CHROM
```




    '2L'




```python
np.bincount(haps_selected[1])
```




    array([1511,   10,    9])




```python
recs = list(tbl_variants_selected.records())
n = len(recs)
ld = np.zeros((n, n), dtype='f8')
for i in range(n):
    i_pos = recs[i].POS
    i_allele = recs[i].ALTIX + 1
    i_vidx = pos_selected.locate_key(i_pos)
    log('row', i, i_vidx, i_pos, i_allele)
    for j in range(i+1, n):
        j_pos = recs[j].POS
        j_allele = recs[j].ALTIX + 1
        j_vidx = pos_selected.locate_key(j_pos)
#         log('col', j, j_vidx, j_pos, j_allele)
        v = lewontin_d_prime(haps_selected, i_vidx, j_vidx, i_allele, j_allele)
#         log('D_prime', v)
        ld[i, j] = v
        ld[j, i] = v
        
```

    row 0 0 2390177 1
    row 1 1 2391228 1
    row 2 1 2391228 2
    row 3 2 2399997 1
    row 4 3 2400071 1
    row 5 3 2400071 2
    row 6 4 2416980 1
    row 7 5 2422651 1
    row 8 6 2422652 1
    row 9 7 2424384 1
    row 10 8 2425077 1
    row 11 9 2429617 1
    row 12 10 2429745 1
    row 13 11 2429897 1
    row 14 12 2429915 1
    row 15 13 2430424 1
    row 16 14 2430817 1
    row 17 15 2430863 1
    row 18 16 2430880 1
    row 19 17 2430881 1
    row 20 18 2431019 1
    row 21 19 2431061 1
    row 22 20 2431079 1



```python
ld[0]
```




    array([ 0.        , -1.        , -1.        , -1.        , -1.        ,
           -1.        , -1.        , -0.9640592 ,  0.91812161, -1.        ,
           -1.        , -1.        , -1.        , -1.        , -1.        ,
           -1.        , -1.        , -1.        , -1.        , -1.        ,
           -1.        , -1.        , -1.        ])




```python
np.isnan(ld[0, 2])
```




    False




```python
s = '44'
```


```python
s.ljust(3)
```




    '44 '




```python
fig = plt.figure(figsize=(7, 6), dpi=120)

gs = mpl.gridspec.GridSpec(1, 2, width_ratios=[7, .5])

# sns.despine(ax=ax, offset=5)
#sns.heatmap(ld, vmin=-1, vmax=1, center=0, square=True, ax=ax, cmap='Blues', cbar_kws=dict(ticks=[-1, -.5, 0, .5, 1]))

ax = fig.add_subplot(gs[0])
im = ax.pcolormesh(ld, vmin=-1, vmax=1, cmap='Blues', shading='flat', edgecolors='gray', linewidths=.5, antialiased=True)

labels = ['%s:%s>%s %s' % (rec.POS, rec.REF, rec.ALT, rec['AGAP004707-RA'].rjust(6))
          for rec in tbl_variants_selected.records()]
# ax.invert_yaxis()
ticks = np.arange(ld.shape[0]) + .5
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(labels, rotation=90, ha='center', va='top', fontdict=dict(family='monospace'))
ax.set_yticklabels(labels, rotation=0, va='center', ha='right', fontdict=dict(family='monospace'));
ax.set_xlim(0, ld.shape[0])
ax.set_ylim(0, ld.shape[0])
ax.xaxis.set_tick_params(length=0)
ax.yaxis.set_tick_params(length=0)
for i in range(ld.shape[0] + 1):
    ax.add_patch(plt.Rectangle((i-1, i-1), 1, 1, color='gray'))
ax.set_title("Linkage disequilibrium (D')", loc='right')

cax = fig.add_subplot(gs[1])
fig.colorbar(im, cax=cax)

fig.tight_layout()
fig.savefig('../artwork/fig_ld.png', dpi=300, bbox_inches='tight');
```


![png](fig_ld_files/fig_ld_31_0.png)



```python

```
