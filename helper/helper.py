import numpy as np

# Utilities
def gen_iid_truncated_normal_utils(n, mean, var):
    pass

def gen_iid_scaled_beta_utils(n=1000, a=1, b=1, low=-1, high=1):
    return np.random.beta(a, b, size=n) * (high-low) + low

def gen_iid_uniform_utils(n, low=-1, high=1):
    return np.random.random(size=n) * (high-low) + low

# Gammas
def gen_uniform_gamma(n):
    x = np.random.random(size=n)
    return x / x.sum()

def gen_normed_beta_gamma(n, a=1, b=1):
    x = np.random.beta(a, b, size=n)
    return x / x.sum()

# Lists

def generate_utils_list(n):
    uts = []
    uts += [gen_iid_scaled_beta_utils(n).tolist()]
    uts += [gen_iid_scaled_beta_utils(n, a=10, b=10).tolist()]
    uts += [gen_iid_scaled_beta_utils(n, a=10).tolist()]
    return uts

def generate_gamma_list(n):
    gs = []
    gs += [gen_uniform_gamma(n).tolist()]
    gs += [gen_normed_beta_gamma(n, a=3).tolist()]
    return gs

