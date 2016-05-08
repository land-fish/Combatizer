
import numpy as np

def maximizer(utility, gamma):
	return np.argmax(utility)

def quantilizer(utility, gamma):
	#sort everything by utility 
	

	#cutoff at q = 0.9

	#sample from gamma

	return np.argmax(utility)

def getAgents():
	return [maximizer, quantilizer]
