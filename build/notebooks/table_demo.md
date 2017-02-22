

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
tbl = etl.wrap(
    [['foo', 'bar', 'baz'],
     [1, 'a', True],
     [2, 'b', False]]
)
tbl
```




<table class='petl'>
<thead>
<tr>
<th>0|foo</th>
<th>1|bar</th>
<th>2|baz</th>
</tr>
</thead>
<tbody>
<tr>
<td style='text-align: right'>1</td>
<td>a</td>
<td>True</td>
</tr>
<tr>
<td style='text-align: right'>2</td>
<td>b</td>
<td>False</td>
</tr>
</tbody>
</table>





```python
prologue = r"""
\begin{tabular}{rll}
\toprule
Foo & Bar & Baz \\
\midrule
"""
template = r"""
{foo} & {bar} & {baz} \\
"""
epilogue = r"""
\bottomrule
\end{tabular}
"""
tbl.totext('../tables/demo.tex', 
           encoding='ascii',
           prologue=prologue, 
           template=template,
           epilogue=epilogue)
```


```python
!cat ../tables/demo.tex
```

    
    \begin{tabular}{rll}
    \toprule
    Foo & Bar & Baz \\
    \midrule
    
    1 & a & True \\
    
    2 & b & False \\
    
    \bottomrule
    \end{tabular}



```python

```
