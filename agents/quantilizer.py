import numpy as np

def quantilizer(q, utility, gamma):
    si = np.argsort(utility) # Sort indices
    sg = np.array(gamma)[si].cumsum() # Commulative probability by utility order
    
    #Pick a random index by cumulative sum over gamma
    r = np.random.random()*q
    for i in range(sg.size):
        if sg[i] > r:
            return i
