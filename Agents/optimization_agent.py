# Agents/optimization_agent.py

from config import AGENT_MAX_ITER, AGENT_MAX_RPM
from crewai import Agent

class OptimizationAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Agente de Otimização de Obtenção de Troféus',
            goal='Otimizar os troféus e criar uma lista um guia com o passo a passo de como conquistar os troféus de forma otimizada.',
            backstory="Especialista em otimizar tempo para alcançar múltiplos troféus simultaneamente e fazer um guia especializado.",
            max_iter=AGENT_MAX_ITER,  # Opcional
            max_rpm=AGENT_MAX_RPM,
            verbose=True
        )
