
class Runner:
	#runner does the following:
	#1. Generate utility function 
	#2. Generate gamma
	#3. Pick comparison metric
	#4. Perturb the thing 
	#5. Pick an agent
	#6. Score an agent 
	
	def run(ut, gamma, comparison, threshold, disturber, agent, scorer):
		uO = perturber(ut, gamma, comparison, threshold) #the utility the agent sees
		actionIndex = agent(u0, gamma) #the index of the action the agent has picked 
		agentScore = ut[actionIndex]
		return agentScore
