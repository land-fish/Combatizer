# code to contain various similarity functions to compare vectors of utility functions

import numpy as np
from scipy import spatial


def centered(u1):
    return (u1 - np.mean(u1)) / np.std(u1)


def getComparisonMetrics():
    def cosine_similarity(u1, u2):
        # standard cosine similarity 
        return 1 - spatial.distance.cosine(u1, u2)

    def centered_cosine_similarity(u1, u2):
        # cosine similarity with a 0 mean
        return cosine_similarity(centered(u1), centered(u2))

    def preference_order_similarity(u1, u2):
        # world preference ordering
        return cosine_similarity(centered(np.argsort(u1)), centered(np.argsort(u2)))

    return [cosine_similarity, centered_cosine_similarity, preference_order_similarity]
