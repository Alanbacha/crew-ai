# Tasks/optimize_guide_task.py

from crewai import Task

class OptimizeGuideTask(Task):
    def __init__(self, game_name):
        super().__init__(
            description=f"Otimizar os guias de troféus para o jogo do PS5: {game_name}",  # Opcional
            expected_output="Guia com lista de atividades para conquistar os troféus de forma otimizada."  # Opcional
        )
