
import numpy as np

def maximizer(utility, gamma):
	return np.argmax(utility)

def getAgents():
	return [maximizer, quantilizer]
