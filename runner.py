from comparison import comparison_functions
from agents import agents
from helper import helper
from perturber import perturber

#comparisons = comparison_functions.getComparisonMetrics()

numWorlds = 100

class Runner:
	#runner does the following:
	#1. Generate utility function 
	#2. Generate gamma
	#3. Pick comparison metric
	#4. Perturb the thing 
	#5. Pick an agent
	#6. Score an agent 
	
	def runAllAgents(s):
		agentList = agents.getAgents()
		return s.generateRun(agentList)
	
	def generateRun(s, agentList):
		#given an agent, pick a random set of ut, gamma, comparison, threshold, 
		uts = helper.generate_utils_list(numWorlds) #list of utilities
		gammas = helper.generate_gamma_list(numWorlds)
		comparisons = comparison_functions.getComparisonMetrics()

		thresholds = [0.95]

		#perturbers = [perturber.Perturber]
		
		agentScores = [0] * len(agentList)
		utGammaCombo = 0
		for ut in uts:
			for gamma in gammas:
				print utGammaCombo
				utGammaCombo += 1
				for comparison in comparisons:
					for threshold in thresholds:
						perturberClass = perturber.Perturber(ut, comparison, threshold)
						perturbers = perturberClass.get_perturbers()
						for pt in perturbers:
							agentIndex = 0 
							u_false = pt() #the utility the agent sees
							for agent in agentList:
								agentScore = s.run(ut, gamma, u_false, agent)
								agentScores[agentIndex] += agentScore
								agentIndex += 1
		return agentScores
	
	def run(s, ut, gamma, u_false, agent):
		u_agent = u_false[:]
		gamma_agent = gamma[:]
		actionIndex = agent(u_agent, gamma_agent) #the index of the action the agent has picked 
		agentScore = ut[actionIndex]
		return agentScore

if __name__=="__main__":
	runner = Runner() 
	print runner.runAllAgents()
	print "PARTY TIME!"
