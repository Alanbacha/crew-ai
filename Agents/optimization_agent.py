# Agents/optimization_agent.py

from config import AGENT_MAX_ITER, AGENT_MAX_RPM
from crewai import Agent

class OptimizationAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Agente de Otimização de Guias',
            goal='Otimizar os guias de troféus e criar um novo guia especializado.',
            backstory="Especialista em otimizar guias para alcançar múltiplos troféus simultaneamente e fazer um Guia especializado.",
            max_iter=AGENT_MAX_ITER,  # Opcional
            max_rpm=AGENT_MAX_RPM
        )
