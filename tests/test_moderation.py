from unittest.mock import Mock
import pytest

from app.moderation import decider


# Test 1 : le message est un spam
def test_message_spam():
    modele = Mock()

    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"

    modele.predict.assert_called_once_with("Offre miracle")


# Test 2 : le message est normal
def test_message_normal():
    modele = Mock()

    modele.predict.return_value = "normal"

    resultat = decider(modele, "Bonjour")

    assert resultat == "autoriser"

    modele.predict.assert_called_once_with("Bonjour")

# Bonus : le modèle rencontre une erreur
def test_modele_indisponible():
    modele = Mock()

    modele.predict.side_effect = RuntimeError(
        "Modele indisponible"
    )

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Offre miracle")
