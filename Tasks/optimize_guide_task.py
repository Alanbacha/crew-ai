# Tasks/optimize_guide_task.py

from crewai import Task
from crewai_tools import WebsiteSearchTool

class OptimizeGuideTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=f"Otimizar e agrupar todas informações obtidas dos troféus, informando o melhor caminho para conquistar o máximo de troféus possívl ao mesmo tempo.",
            agent=agent,
            expected_output="Guia com uma lista do passo a passo de como conquistar os troféus de forma otimizada.",
            tools=[WebsiteSearchTool()]
        )
