# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:23:30 2017

@author: providence
"""

import numpy as np
from scipy.spatial.distance import pdist,squareform
import matplotlib.pyplot as plt
import time

L   = 100       # simulation box dimension
N   = int(1e3)       # Number of particles
dim = 2         # Dimensions

# Generate random positions of particles
r = (np.random.random(size=(N,dim))-0.5)*L

t1 = time.time()
# Compute distance matrix
D = np.zeros(shape=(N,N), dtype=float)
#c=0
# This is the N-squared operation
for i in range(N):
    for j in range(i+1,N):
        dr = r[j]-r[i]                  # difference between 2 positions
        D[i,j] = np.sqrt(sum(dr*dr))    # calculate distance and store

print(time.time()-t1)
        #c=c+1
#print(c)

#DD = pdist(r)

#print(D[:3,:3])

#print("******")
#print(squareform(DD)[0])
