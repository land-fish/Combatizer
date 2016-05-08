class Runner:
	#runner does the following:
	#1. Generate utility function 
	#2. Generate gamma
	#3. Pick comparison metric
	#4. Perturb the thing 
	#5. Pick an agent
	#6. Score an agent 

	def generateRun(agent1, agent2):
		#given an agent, pick a random set of ut, gamma, comparison, threshold, 
		uts = generateUts() #list of utilities
		gammas = generateGammas()
		comparisons = getComparisonMetrics()
		thresholds = generateThresholds()
		perturbers = generatePerturbers()
		diff = 0
		for ut in uts:
			for gamma in gammas:
				for comparison in comparisons:
					for threshold in threshold:
						for perturber in perturbers:
							agentScore1 = this.run(ut, gamma, comparison, threshold, perturber, agent1)
							agentScore2 = this.run(ut, gamma, comparison, threshold, perturber, agent2)
							diff = agentScore1 - agentScore2
		return diff
	
	def run(ut, gamma, comparison, threshold, disturber, agent):
		uO = perturber(ut, gamma, comparison, threshold) #the utility the agent sees
		actionIndex = agent(u0, gamma) #the index of the action the agent has picked 
		agentScore = ut[actionIndex]
		return agentScore
