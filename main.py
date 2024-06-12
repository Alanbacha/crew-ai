from Crews.trophy_guide.crew import TrophyGuideCrew

def main():
    # Criar e inicializar a equipe
    trophy_crew = TrophyGuideCrew()
    result = trophy_crew.execute()
    print(result)

if __name__ == "__main__":
    main()