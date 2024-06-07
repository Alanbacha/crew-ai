# Tasks/search_guides_task.py

from crewai import Task
from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool, YoutubeVideoSearchTool

class SearchGuidesTask(Task):
    def __init__(self, agent, game_name):
        super().__init__(
            description=f"Buscar informações de como conquistar todos os troféus do PS5 para o jogo {game_name}",
            agent=agent,
            expected_output="Lista com todas as informações de como conquistar todos os troféus do jogo.",
            tools=[ScrapeWebsiteTool(), WebsiteSearchTool(), YoutubeVideoSearchTool()]
        )
