# Tasks/search_guides_task.py

from crewai import Task

class SearchGuidesTask(Task):
    def __init__(self, game_name):
        super().__init__(
            description=f"Buscar guias de troféus para o jogo do PS5: {game_name}",  # Opcional
            expected_output="Lista com os melhores guias de troféus para o jogo PS5."  # Opcional
        )
