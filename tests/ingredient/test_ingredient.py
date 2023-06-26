from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


def test_ingredient():
    farinha_trigo = Ingredient("farinha")
    farinha = Ingredient("farinha")
    camarao = Ingredient("camarão")
    assert hash(farinha_trigo) == hash(farinha)
    assert hash(farinha_trigo) != hash(camarao)
    assert camarao == camarao
    assert farinha_trigo != camarao
    assert repr(farinha_trigo) == "Ingredient('farinha')"
    assert camarao.name == "camarão"
    assert farinha_trigo.restrictions == {Restriction.GLUTEN}
