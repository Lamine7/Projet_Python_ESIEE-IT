from qcm.question import Question 
from qcm.quiz import Quiz          

def creer_questions():
    """
    Créatioon d'une liste d'objets Question pour le quiz
    """
    return [
        Question("Qui a remporté la Coupe du Monde 2018 ?", ["France", "Brésil", "Allemagne"], "a"),
        Question("Quel est le joueur avec le plus de Ballons d'Or ?", ["Cristiano Ronaldo", "Lionel Messi", "Michel Platini"], "b"),
        Question("Quel pays a organisé les Jeux Olympiques de 2020 ?", ["Brésil", "Japon", "Chine"], "b"),
        Question("Quel joueur de football a marqué le plus de buts en Coupe du Monde ?", ["Pele", "Ronaldo", "Miroslav Klose"], "c"),
        Question("Combien de joueurs composent une équipe de basketball sur le terrain ?", ["5", "6", "7"], "a"),
        Question("Quel est le plus grand nombre de points marqués en un seul match NBA ?", ["81", "100", "92"], "b"),
        Question("Qui a remporté le plus grand nombre de titres de MVP en NBA ?", ["LeBron James", "Michael Jordan", "Kareem Abdul-Jabbar"], "c"),
        Question("En quelle année Michael Jordan a-t-il pris sa première retraite du basket ?", ["1993", "1996", "2001"], "a"),
        Question("Qui est l'entraîneur des Golden State Warriors en 2020 ?", ["Steve Kerr", "Phil Jackson", "Gregg Popovich"], "a"),
        Question("Combien d'équipes participent à la Ligue des Champions de football ?", ["32", "64", "16"], "a"),
    ]

def main():
    """
    Voiici la fonction principale pour exécuter le quiz
    """
    questions = creer_questions()
    quiz = Quiz(questions)
    quiz.lancer()
    quiz.afficher_resultat()

if __name__ == "__main__":
    main()
