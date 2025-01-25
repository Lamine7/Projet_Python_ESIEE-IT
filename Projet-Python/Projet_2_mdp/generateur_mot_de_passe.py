import random
import string
from testeur_mot_de_passe import TesteurMotDePasse

class GenerateurMotDePasse:
    """"
     Fonction pour la génération d'un mot de passe aléatoire
    """
    @staticmethod
    def generer_mot_de_passe(nb_minuscules, nb_majuscules, nb_chiffres, nb_speciaux):
        caracteres_mdp = (
            random.choices(string.ascii_lowercase, k=nb_minuscules) +  # Ajout de lettres minuscules
            random.choices(string.ascii_uppercase, k=nb_majuscules) +  # Ajout de lettres majuscules
            random.choices(string.digits, k=nb_chiffres) +  # Ajout de chiffres
            random.choices(string.punctuation, k=nb_speciaux)  # Ajout de caractères spéciaux
        )
        random.shuffle(caracteres_mdp)  # Mélange des caractères pour plus de sécurité
        mot_de_passe = ''.join(caracteres_mdp)
        entropie = TesteurMotDePasse.calculer_entropie(mot_de_passe)
        force = TesteurMotDePasse.evaluer_force(entropie)
        conforme_politique = TesteurMotDePasse.verifier_politique(mot_de_passe)
        return mot_de_passe, entropie, force, conforme_politique