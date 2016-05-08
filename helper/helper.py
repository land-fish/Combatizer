import numpy as np

def gen_iid_scaled_beta_utils(n=1000, a=1, b=1, low=-1, high=1):
    return np.random.beta(a, b, size=n) * (high-low) + low

def gen_iid_uniform_utils(n, low=-1, high=1):
    return np.random.random(size=n) * (high-low) + low

def gen_true_utils(n):
    return gen_iid_scaled_beta_utils(n=n, a=5, b=5)

