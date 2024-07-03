from Crews.book_series.crew import BookSeriesCrew
from Crews.trophy_guide.crew import TrophyGuideCrew

def main():
    # Criar e inicializar a equipe
    bookSeriesCrew = BookSeriesCrew()
    result = bookSeriesCrew.execute()
    print(result)
    
    # Criar e inicializar a equipe
    # trophyGuideCrew = TrophyGuideCrew()
    # result = trophyGuideCrew.execute()
    # print(result)

if __name__ == "__main__":
    main()