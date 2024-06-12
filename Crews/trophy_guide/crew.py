from config import CREW_MAX_RPM
from crewai import Crew
from Crews.trophy_guide.agents import Agents
from Crews.trophy_guide.tasks import Tasks


class TrophyGuideCrew():
	crew:Crew
	game_name:str

	def __init__(self):
		self.game_name = input("Digite o nome do jogo: ")

		# Agente de busca
		searchAgent = Agents.Search
		searchTask = Tasks.Search
		searchTask.agent= searchAgent

		# Agente de otimização
		optimizationAgent = Agents.Optimization
		optimizationTask = Tasks.Optimization
		optimizationTask.agent= optimizationAgent

		self.crew = Crew(
			agents = [searchAgent, optimizationAgent],
			tasks = [searchTask, optimizationTask],
			max_rpm = CREW_MAX_RPM,
			verbose = True
		)

		# Tasks.Search.agent = Agents.Search
		# Tasks.Optimization.agent = Agents.Optimization

		# self.crew = Crew(
		# 	agents = [Agents.Search, Agents.Optimization],
		# 	tasks = [Tasks.Search, Tasks.Optimization],
		# 	max_rpm = CREW_MAX_RPM,
		# 	verbose = True
		# )

	def execute(self):
		result = self.crew.kickoff(inputs={"game_name":self.game_name})

		return result
