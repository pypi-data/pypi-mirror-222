# ARCU
Find representative subpopulations in single cell imaging data. 
​
## Introduction
ARCU is a simple algorithm for finding coordinates in single-cell imaging data where measured features are relatively variable. This is a useful task for finding representative images for publication that illustrate difference in cell types. ARCU finds regions in an image where cells are different; in other words, it finds regions where at least one cell is above a threshold and at least one cell is below a threshold for features of interest. Thresholds are given by:

    mu + u*sig
    mu - u*sig

where 
```
mu = mean expression for feature across whole population
sig = standard deviation for feature across whole population
u = a scaling coefficent
```
​​
## Installation
Dependencies 
* Python >= 3.6, numpy >= 1.22.4, pandas >= 1.3.2
​
You can install the package and necessary dependencies with `pip` by,
```
pip install arcu
```
​
## Example use
To find regions of interest using ARCU, first read in a pandas dataframe formatted such that the first column is numeric labels, the second is x-coordinates, the third is y-coordinates, and columns 4 through n are features of interest. Rows should be interpretable as "cells" profiled from segmented images with single-cell resolution. 
​
```python
import pandas
A = pandas.read_csv('dir/file.csv')
```
​
Then execute ARCU using

```python
import arcu
centroids = arcu.arcu(A,r,c,u)
```

where 
```
Inputs:
  A = dataframe of single cell location and feature data
  r = radius, in pixels, of regions in which to search for subpopulations
  c = the minimum number of cells a region of interest can contain to be considered for reporting
  u = the scaling coefficient on standard deviation for a cell to be considered interesting

Returns:
  a dataframe containing the x,y coordinates of groupings that meet feature expression criteria
```
