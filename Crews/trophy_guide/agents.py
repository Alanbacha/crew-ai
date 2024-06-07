from config import AGENT_MAX_ITER, AGENT_MAX_RPM
from crewai import Agent

class TrophyGuideSearchAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Especialista em Pesquisa de Troféus de Jogos do PS5',
            goal='Buscar e coletar informações detalhadas sobre troféus de jogos do PS5.',
            backstory="Este agente é especializado em encontrar guias completos de troféus para jogos, pesquisando na internet para coletar informações detalhadas e precisas.",
            max_iter=AGENT_MAX_ITER,
            max_rpm=AGENT_MAX_RPM,
            verbose=True
        )

class TrophyGuideOptimizationAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Especialista em Roadmap de Troféus de Jogos no PS5',
            goal='Ler listas de troféus e criar um roadmap otimizado para obter todos os troféus do jogo da forma mais eficiente.',
            backstory="Este agente é um especialista em análise e otimização de estratégias para a obtenção de troféus em jogos de PS5, desenvolvendo guias detalhados que permitem aos jogadores alcançar todos os troféus de maneira rápida e eficiente.",
            max_iter=AGENT_MAX_ITER,
            max_rpm=AGENT_MAX_RPM,
            verbose=True
        )