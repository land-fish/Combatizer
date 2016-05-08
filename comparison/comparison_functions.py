# code to contain various similarity functions to compare vectors of utility functions

import numpy as np
from scipy import spatial
from scipy.stats import spearmanr

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

    def spearman(u1, u2):
        # calculates Spearman's rank correlation coefficient
        # NOTE: result[0] returns the calculated value, we also have access to the corresponding p-value (would be in result[1], not being returned)
        result = spearmanr(u1,u2)
        return result[0]

    # these four functions calculate the LN norm of the difference vector (where N = 1, 2, inf, -inf)
    def l1_norm(u1, u2):
        difference_vector = np.divide(np.subtract(u1, u2), 2)
        return 1 - (np.linalg.norm(difference_vector, 1) * (1/len(u1)))

    def l2_norm(u1, u2):
        difference_vector = np.divide(np.subtract(u1, u2), 2)
        return 1 - (np.linalg.norm(difference_vector, 2) * (1/len(u1)))
        # return 1 - np.linalg.norm(difference_vector, 2)

    def positive_inf_norm(u1, u2):
        difference_vector = np.divide(np.subtract(u1, u2), 2)
        return 1 - np.linalg.norm(difference_vector, np.inf)
    
    def negative_inf_norm(u1, u2):
        difference_vector = np.divide(np.subtract(u1, u2), 2)
        return 1 - np.linalg.norm(difference_vector, -np.inf)

            
    
    return [cosine_similarity,
            centered_cosine_similarity,
            preference_order_similarity,
            spearman]

            #l1_norm,
            #l2_norm,
            #positive_inf_norm,
            #negative_inf_norm]
