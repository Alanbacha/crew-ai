from crewai import Task
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool

# Instantiate tools
directoryReadTool = DirectoryReadTool(directory='./stories')
fileReadTool = FileReadTool()
serperDevTool = SerperDevTool()
websiteSearchTool = WebsiteSearchTool()

class Tasks():
	# Tarefas para o Escritor de Livros Infantis
	WriteStory = Task(
		description="""
			Criar uma história infantil encantadora utilizando os seguintes elementos:
			1. Personagens principais sendo animais com personalidades relacionadas às suas características reais.
			2. Um enredo simples e cativante que aborda temas do dia a dia das crianças.
			3. Uma moral ou lição que as crianças possam aprender ao final da história.
		""",
		expected_output="""
			Uma história infantil completa e envolvente com:
			1. Título cativante.
			2. Introdução dos personagens e suas personalidades.
			3. Enredo principal que mantém a atenção das crianças.
			4. Conclusão com uma moral clara.
		""",
		tools=[directoryReadTool, fileReadTool]
	)
	
	CharacterDevelopment = Task(
		description="""
			Desenvolver personalidades detalhadas para os personagens animais, com base em suas características reais.
		""",
		expected_output="""
			Descrições detalhadas de cada personagem animal, incluindo:
			1. Nome do personagem.
			2. Espécie do animal.
			3. Personalidade e características principais.
			4. Papel na história.
		""",
		tools=[fileReadTool]
	)

	# Tarefas para o Revisor Ortográfico e Gramatical
	ProofreadStory = Task(
		description="""
			Revisar a história infantil escrita para garantir que esteja livre de erros ortográficos e gramaticais.
			Certificar-se de que a linguagem esteja adequada para crianças.
		""",
		expected_output="""
			Texto revisado com:
			1. Correção de todos os erros ortográficos e gramaticais.
			2. Ajustes na linguagem para garantir que seja adequada para o público infantil.
			3. Comentários sobre quaisquer ajustes significativos feitos.
		""",
		tools=[fileReadTool]
	)

	TranslateStory = Task(
		description="""
			Traduzir a história infantil revisada para inglês e francês.
		""",
		expected_output="""
			Versões traduzidas da história em:
			1. Inglês.
			2. Francês.
		""",
		tools=[serperDevTool]
	)

	# Tarefas para o Pedagogo Infantil
	EducationalReview = Task(
		description="""
			Revisar a história infantil para garantir que ela incorpora elementos educacionais apropriados para crianças de até 12 anos.
		""",
		expected_output="""
			Feedback detalhado sobre:
			1. Elementos educacionais presentes na história.
			2. Sugestões de melhorias para aumentar o valor educacional.
			3. Confirmação de que a moral da história é adequada e benéfica para o público infantil.
		""",
		tools=[websiteSearchTool]
	)

	AddEducationalElements = Task(
		description="""
			Adicionar elementos educacionais à história infantil, baseando-se no feedback do pedagogo.
		""",
		expected_output="""
			História infantil revisada com:
			1. Novos elementos educacionais incorporados.
			2. Ajustes feitos conforme o feedback pedagógico.
			3. Explicação de como os novos elementos educacionais beneficiam as crianças.
		""",
		tools=[directoryReadTool, fileReadTool]
	)

	# Tarefas para o Criador de Séries de Livros Infantis
	CreateBookStructure = Task(
		description="""
			Criar a estrutura completa de um livro infantil, incluindo:
			1. Descrição da capa do livro.
			2. Título do livro.
			3. Número da série.
			4. Sinopse.
			5. Apresentação.
			6. Capítulos, com títulos e conteúdo.
			Garantir que cada livro tenha pelo menos 10 capítulos e cada capítulo tenha pelo menos 5 parágrafos.
		""",
		expected_output="""
			Estrutura completa do livro infantil com:
			1. Texto descrevendo a capa.
			2. Título.
			3. Número da série.
			4. Sinopse.
			5. Apresentação.
			6. Capítulos detalhados, com títulos e conteúdo.
		""",
		tools=[directoryReadTool, fileReadTool, serperDevTool, websiteSearchTool]
	)
