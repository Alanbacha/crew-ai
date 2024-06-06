# Agents/guide_search_agent.py

from config import AGENT_MAX_ITER, AGENT_MAX_RPM
from crewai import Agent
from crewai_tools import WebsiteSearchTool

website_search_tool = WebsiteSearchTool()

class GuideSearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Agente de Pesquisa de Guias',
            goal='Encontrar guias de troféus para PS5.',
            backstory="Especialista em encontrar guias de troféus na internet.",
            max_iter=AGENT_MAX_ITER,  # Opcional
            max_rpm=AGENT_MAX_RPM,
            tools=[website_search_tool]
        )
