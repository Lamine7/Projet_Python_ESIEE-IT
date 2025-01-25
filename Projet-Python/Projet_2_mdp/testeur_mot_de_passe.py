import math
import string

class TesteurMotDePasse:
    """
     Fonction pour calculer l'entropie d'un mot de passe
    """
    @staticmethod
    def calculer_entropie(mot_de_passe):
        taille_jeu_caracteres = 0
        if any(c.islower() for c in mot_de_passe):
            taille_jeu_caracteres += 26  # Ajout des minuscules
        if any(c.isupper() for c in mot_de_passe):
            taille_jeu_caracteres += 26  # Ajout des majuscules
        if any(c.isdigit() for c in mot_de_passe):
            taille_jeu_caracteres += 10  # Ajout des chiffres
        if any(c in string.punctuation for c in mot_de_passe):
            taille_jeu_caracteres += len(string.punctuation)  # Ajout des caractères spéciaux
        
        """
         Calcul de l'entropie en fonction de la longueur et de la taille du jeu de caractères
        """
        entropie = len(mot_de_passe) * math.log2(taille_jeu_caracteres)
        return entropie
    
    """
     Fonction pour évaluer la force d'un mot de passe
    """
    @staticmethod
    def evaluer_force(entropie):
        if entropie < 35:
            return "Faible"
        elif entropie < 60:
            return "Moyen"
        else:
            return "Fort"
    
    """
     Vérification de la conformité aux recommandations de l'ANSSI
    """
    @staticmethod
    def verifier_politique(mot_de_passe):
        longueur_ok = len(mot_de_passe) >= 12  # Longueur minimale recommandée par l'ANSSI
        complexite_ok = (
            any(c.islower() for c in mot_de_passe) and
            any(c.isupper() for c in mot_de_passe) and
            any(c.isdigit() for c in mot_de_passe) and
            any(c in string.punctuation for c in mot_de_passe)
        )
        return longueur_ok and complexite_ok