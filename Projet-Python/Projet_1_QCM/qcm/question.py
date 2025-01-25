class Question:
    def __init__(self, texte, options, reponse_correcte):
        """
        Initialisation d'une question
        :param texte: texte de la question
        :param options: liste de 3 options (a, b, c)
        :param reponse_correcte: La réponse correcte ('a', 'b', ou 'c')
        """
        self.texte = texte
        self.options = options
        self.reponse_correcte = reponse_correcte.lower()

    def is_correct(self, reponse_utilisateur):
        """
        Vérification si la réponse de l'utilisateur est bonne
        :param reponse_utilisateur: Réponse donnée par l'utilisateur ('a', 'b', 'c')
        :return: True si correct, False sinon
        """
        return reponse_utilisateur.lower() == self.reponse_correcte