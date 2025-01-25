from generateur_mot_de_passe import GenerateurMotDePasse
from passphrase_generator import PassphraseGenerator

# Programme principal
if __name__ == "__main__":
    mot_de_passe, entropie, force, conforme_politique = GenerateurMotDePasse.generer_mot_de_passe(4, 4, 4, 4)
    print(f"Mot de passe: {mot_de_passe}\n Entropie: {entropie:.2f}\n Force: {force}\n Conforme ANSSI: {conforme_politique}")
    
    phrase_de_passe, entropie, force = PassphraseGenerator.generer_phrase_de_passe()
    print(f"Phrase de passe: {phrase_de_passe}\n Entropie: {entropie:.2f}\n Force: {force}")
