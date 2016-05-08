# code to contain various similarity functions to compare vectors of utility functions

import numpy as np
from scipy import spatial

def centered(u1):
    return (u1 - np.mean(u1)) / np.std(u1)

def similarity(u1, u2, version = 'cosine'):

    # standard cosine similarity 
    if version == 'cosine':
        return 1 - spatial.distance.cosine(u1, u2)

    # cosine similarity with a 0 mean
    if version == 'centered':
        return similarity(centered(u1), centered(u2))

    # world preference ordering
    if version == 'preference order':
        return similarity(centered(np.argsort(u1)), centered(np.argsort(u2)))

