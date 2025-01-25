import random
import math
from testeur_mot_de_passe import TesteurMotDePasse

class PassphraseGenerator:
    # Génération de phrase de passe basée sur la méthode des dés EFF
    @staticmethod
    def generer_phrase_de_passe(nb_mots=6):
        with open("Projet_2_mdp/eff_large_wordlist.txt") as f:
            liste_mots = {line.split()[0]: line.split()[1] for line in f}
        
        phrase_de_passe = []
        for _ in range(nb_mots):
            mot_aleatoire = str(random.randint(11111, 66666))
            while mot_aleatoire not in liste_mots:
                mot_aleatoire = str(random.randint(11111, 66666))
            phrase_de_passe.append(liste_mots[mot_aleatoire])
        
        phrase_de_passe = ' '.join(phrase_de_passe)
        entropie = nb_mots * math.log2(len(liste_mots))
        force = TesteurMotDePasse.evaluer_force(entropie)
        return phrase_de_passe, entropie, force