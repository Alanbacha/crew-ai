from crewai import Task
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool, YoutubeVideoSearchTool

class TrophyGuideSearchTask(Task):
    def __init__(self, agent, game_name):
        super().__init__(
            description=f"""
                Tendo como base o jogo do PS5: {game_name}.
                Buscar informações detalhadas sobre como obter todos os troféus do jogo.
                Encontrar e coletar informações sobre cada troféu, incluindo nome, raridade, descrição, método de obtenção, dificuldade e possíveis estratégias para obter o troféu.
            """,
            agent=agent,
            expected_output="""
                Lista completa de todos os troféus do jogo. Cada entrada da lista deve conter:
                1. Nome do troféu
                2. Raridade do troféu
                3. Descrição do que precisa ser feito para obter o troféu
                4. Método detalhado de obtenção do troféu
                5. Avaliação da dificuldade para obter o troféu
                6. Estratégias possíveis para facilitar a obtenção do troféu
                7. Referências e fontes das informações coletadas
            """,
            tools=[ScrapeWebsiteTool(), WebsiteSearchTool(), YoutubeVideoSearchTool()]
        )

class TrophyGuideOptimizationTask(Task):
    def __init__(self, agent, game_name):
        super().__init__(
            description=f"""
                Tendo como base o jogo do PS5: {game_name}.
                Ler listas de troféus de um jogo e criar um roadmap completo para obter todos os troféus do jogo de maneira mais eficiente e performática possível.
                Analisar as listas de troféus, identificar possíveis combinações e sequências de ações que permitem obter múltiplos troféus ao mesmo tempo, e desenvolver um guia detalhado e otimizado.
            """,
            expected_output="""
                Guia completo e otimizado para a obtenção de troféus do jogo.
                O guia deve incluir:
                1. Um roadmap passo a passo detalhado para obter todos os troféus da forma mais eficiente.
                2. Cada passo deve descrever as ações necessárias e indicar quais troféus serão obtidos.
                3. Recomendações sobre como combinar ações para obter múltiplos troféus ao mesmo tempo.
                4. Estratégias específicas para otimizar o tempo e os recursos durante a obtenção dos troféus.
                5. Dicas adicionais para superar desafios específicos ou evitar obstáculos comuns.
            """,
            agent=agent,
            tools=[WebsiteSearchTool()]
        )