

```python
%run setup.ipynb
```


<style type="text/css">
.container {
    width: 100%;
}
div#notebook {
    padding-top: 0;
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
#site {
    height: auto !important;
}
</style>



```python
%%bash
# copy the specific regions haplotypes from phase 1 into the repo, as they are small
for f in ../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3.1/haplotypes/specific_regions/PARA/*; do
    cp -v --no-clobber $f ../data/ag1000g.phase1.AR3.1.haplotypes.specific_regions.`basename $f`
done
```


```python

```
