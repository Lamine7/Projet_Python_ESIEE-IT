import random
from qcm.question import Question  # Import modifié pour respecter la structure

class Quiz:
    def __init__(self, questions):
        """
        Inatialisation du quiz
        :param questions: Liste d'objets Question
        """
        self.questions = questions
        self.score = 0

    def lancer(self):
        """
        Démarre le quiz avec des questions posées aléatoirement
        """
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.texte}")
            print(f"a) {question.options[0]}")
            print(f"b) {question.options[1]}")
            print(f"c) {question.options[2]}")

            reponse = input("Votre réponse (a, b, c) : ").strip().lower()
            if question.is_correct(reponse):
                print("Bravo, bonne réponse !\n")
                self.score += 1
            else:
                print(f"OUPS, Mauvaise réponse. La bonne réponse était : {question.reponse_correcte}\n")

    def afficher_resultat(self):
        """
        Affiche le score final ainsi que le corrigé
        """
        print(f"Merci d'avoir joué. Votre score final est : {self.score}/{len(self.questions)}")
        print("\nCorrigé :")
        for question in self.questions:
            print(f"{question.texte} - Réponse correcte : {question.reponse_correcte}")