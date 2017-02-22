
This is an example notebook. It depends on some external data resources, and so cannot be run during continuous integration checks. It extracts some data from an external source, then saves to a local file, which will get checked in to the GitHub repo.


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
callset = zarr.open_group('../ngs.sanger.ac.uk/production/ag1000g/phase1/AR3.1/variation/main/zarr2/ag1000g.phase1.ar3', mode='r')
callset
```




    Group(/, 8)
      arrays: 1; samples
      groups: 7; 2L, 2R, 3L, 3R, UNKN, X, Y_unplaced
      store: DirectoryStore




```python
extract = callset['2L/calldata/genotype'][:1000]
extract
```




    array([[[-1, -1],
            [-1, -1],
            [-1, -1],
            ..., 
            [ 0,  0],
            [-1, -1],
            [-1, -1]],
    
           [[-1, -1],
            [-1, -1],
            [-1, -1],
            ..., 
            [-1, -1],
            [-1, -1],
            [-1, -1]],
    
           [[-1, -1],
            [-1, -1],
            [-1, -1],
            ..., 
            [-1, -1],
            [-1, -1],
            [-1, -1]],
    
           ..., 
           [[ 0,  0],
            [ 0,  0],
            [ 0,  0],
            ..., 
            [ 0,  0],
            [ 0,  0],
            [ 0,  0]],
    
           [[ 0,  0],
            [ 0,  0],
            [ 0,  0],
            ..., 
            [ 0,  0],
            [ 0,  0],
            [ 0,  0]],
    
           [[ 0,  0],
            [ 0,  0],
            [ 0,  0],
            ..., 
            [ 0,  0],
            [ 0,  0],
            [ 0,  0]]], dtype=int8)




```python
import numpy as np
```


```python
np.save('../data/demo.npy', extract)
```


```python

```
