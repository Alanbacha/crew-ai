from config import CREW_MAX_RPM
from crewai import Crew
from Crews.book_series.agents import Agents
from Crews.book_series.tasks import Tasks

class BookSeriesCrew():
    crew: Crew

    def __init__(self):
        # Agente Escritor
        writerAgent = Agents.Writer
        writeStoryTask = Tasks.WriteStory
        writeStoryTask.agent = writerAgent

        characterDevelopmentTask = Tasks.CharacterDevelopment
        characterDevelopmentTask.agent = writerAgent

        # Agente Revisor
        proofreaderAgent = Agents.Proofreader
        proofreadStoryTask = Tasks.ProofreadStory
        proofreadStoryTask.agent = proofreaderAgent

        translateStoryTask = Tasks.TranslateStory
        translateStoryTask.agent = proofreaderAgent

        # Agente Educador
        educatorAgent = Agents.Educator
        educationalReviewTask = Tasks.EducationalReview
        educationalReviewTask.agent = educatorAgent

        addEducationalElementsTask = Tasks.AddEducationalElements
        addEducationalElementsTask.agent = educatorAgent

        # Agente Criador de Séries
        seriesCreatorAgent = Agents.SeriesCreator
        createBookStructureTask = Tasks.CreateBookStructure
        createBookStructureTask.agent = seriesCreatorAgent

        self.crew = Crew(
            agents=[
                writerAgent, 
                proofreaderAgent, 
                educatorAgent, 
                seriesCreatorAgent
            ],
            tasks=[
                writeStoryTask, 
                characterDevelopmentTask, 
                proofreadStoryTask, 
                translateStoryTask, 
                educationalReviewTask, 
                addEducationalElementsTask, 
                createBookStructureTask
            ],
            max_rpm=CREW_MAX_RPM,
            verbose=True
        )

    def execute(self):
        result = self.crew.kickoff()
        return result
