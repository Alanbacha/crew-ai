from config import CREW_MAX_RPM
from crewai import Crew
from Crews.trophy_guide.agents import TrophyGuideSearchAgent, TrophyGuideOptimizationAgent
from Crews.trophy_guide.tasks import TrophyGuideSearchTask, TrophyGuideOptimizationTask

class TrophyGuideCrew(Crew):
	def __init__(self):
		game_name = input("Digite o nome do jogo: ")

		# Agents
		searchAgent = TrophyGuideSearchAgent()
		optimizationAgent = TrophyGuideOptimizationAgent()

		# Tasks
		searchTask = TrophyGuideSearchTask(searchAgent, game_name)
		optimizationTask = TrophyGuideOptimizationTask(optimizationAgent, game_name)

		super().__init__(
			agents = [searchAgent, optimizationAgent],
			tasks = [searchTask, optimizationTask],
			language = "Portuguese",
			max_rpm = CREW_MAX_RPM,
			verbose = True
		)

	def execute(self):
		result = self.kickoff(inputs={})
		print(result)
		return result
