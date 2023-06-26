import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    manteiga = Dish("manteiga", 22.40)
    rice = Dish("arroz", 15.50)
    arroz = Ingredient('arroz')
    with pytest.raises(ValueError):
        Dish('Camarão', -1035)
    assert hash(manteiga) != hash(rice)
    assert hash(rice) == hash(rice)
    assert manteiga.name == 'manteiga'
    assert rice == rice
    manteiga.add_ingredient_dependency(arroz, 15)
    assert arroz in manteiga.get_ingredients()
    assert manteiga.get_restrictions() == set()
    assert manteiga.__repr__() == "Dish('manteiga', R$22.40)"
