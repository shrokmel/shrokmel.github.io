# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:18:22 2017

@author: providence
"""

import numpy as np
from scipy.spatial.distance import pdist,squareform
import matplotlib.pyplot as plt

L   = 100       # simulation box dimension
N   = 1000       # Number of particles
dim = 2         # Dimensions

# Generate random positions of particles
r = (np.random.random(size=(N,dim))-0.5)*L


t1 = time.time()        
uti = np.triu_indices(100, k=1)         # upper triangular indices
a = np.square(r[uti[0]]-r[uti[1]])
a = np.sqrt(np.sum(a,axis=1))

print(time.time()-t1)

t1 = time.time()   
DD = pdist(r)
print(time.time()-t1)

print(a,DD)