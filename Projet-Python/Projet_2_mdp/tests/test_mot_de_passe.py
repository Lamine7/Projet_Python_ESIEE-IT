import pytest
from testeur_mot_de_passe import TesteurMotDePasse

def test_entropie():
    assert TesteurMotDePasse.calculer_entropie("Aa1!") > 0
