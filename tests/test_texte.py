from tkinter import _test
import pytest

from app.texte import nettoyer_texte

def test_nettoyer_texte():
    assert nettoyer_texte("  Bonjours  ENIAD ") == "bonjours eniad"


@ pytest.mark.parametrize("entree, attendu", 
[
    ("  BONJOUR    monde  ", "bonjour monde"),
    ("déjà propre", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("BONJOUR", "bonjour")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu



def test_nettoyer_texte_nombre():
    with pytest.raises(TypeError):
        nettoyer_texte(123)


def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)
