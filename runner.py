from comparison import comparison_functions
from agents import agents
from helper import helper

#comparisons = comparison_functions.getComparisonMetrics()

class Runner:
	#runner does the following:
	#1. Generate utility function 
	#2. Generate gamma
	#3. Pick comparison metric
	#4. Perturb the thing 
	#5. Pick an agent
	#6. Score an agent 
	
	def runAllAgents():
		agentList = agents.getAgents()
		generateRun(agentList)
	
	def generateRun(agentList):
		#given an agent, pick a random set of ut, gamma, comparison, threshold, 
		uts = generateUts() #list of utilities
		gammas = generateGammas()
		comparisons = comparison.getComparisonMetrics()
		thresholds = generateThresholds()
		perturbers = generatePerturbers()
		
		agentScores = [0]* len(agentList)
		for ut in uts:
			for gamma in gammas:
				for comparison in comparisons:
					for threshold in threshold:
						for perturber in perturbers:
							agentIndex = 0 
							for agent in agentList:
								agentScore = this.run(ut, gamma, comparison, threshold, perturber, agent)
								agentScores[agentIndex] += agentScore
								agentIndex += 1
		return agentScores
	
	def run(ut, gamma, comparison, threshold, disturber, agent):
		uO = perturber(ut, gamma, comparison, threshold) #the utility the agent sees
		actionIndex = agent(u0, gamma) #the index of the action the agent has picked 
		agentScore = ut[actionIndex]
		return agentScore
