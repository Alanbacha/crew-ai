# Agents/guide_search_agent.py

from config import AGENT_MAX_ITER, AGENT_MAX_RPM
from crewai import Agent

class GuideSearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Agente de Pesquisa de Troféus do PS5',
            goal='Encontrar guias de troféus para PS5.',
            backstory="Especialista em encontrar guias de troféus na internet.",
            max_iter=AGENT_MAX_ITER,
            max_rpm=AGENT_MAX_RPM,
            verbose=True
        )
