# Crews/trophy_guides_crew.py

from config import CREW_MAX_RPM
from crewai import Crew
from Agents.guide_search_agent import GuideSearchAgent
from Agents.optimization_agent import OptimizationAgent
from Tasks.optimize_guide_task import OptimizeGuideTask
from Tasks.search_guides_task import SearchGuidesTask

class TrophyGuidesCrew(Crew):
	def __init__(self):
		game_name = input("Digite o nome do jogo: ")

		super().__init__(
			agents=[
				GuideSearchAgent(),
				OptimizationAgent()
			],
			tasks=[
				SearchGuidesTask(game_name),
				OptimizeGuideTask(game_name)
			],
			language="Portuguese",
			max_rpm=CREW_MAX_RPM
		)

	def execute(self):
		result = self.kickoff(inputs={})
		print(result)
		return result
