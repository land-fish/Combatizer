
class Runner:
	#runner does the following:
	#1. generate utility function 
	#2. Generate gamma
	#3. pick comparison metric
	#4. Distrub the thing 
	#5. Pick an agent
	#6. Score an agent 
	
	def run(ut, gamma, comparison, threshold, disturber, agent, scorer):
		uO = distruber(ut, gamma, comparison, threshold) #the utility the agent sees
		actionIndex = agent(u0, gamma) #the index of the action the agent has picked 
		agentScore = ut[actionIndex]
		return agentScore
