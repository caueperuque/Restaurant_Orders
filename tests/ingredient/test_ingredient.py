from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Teste para um ingrediente com restrições conhecidas
    ingredient = Ingredient("queijo mussarela")
    ingredient1 = Ingredient("queijo mussarela")
    ingredient_test = Ingredient("carne")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {
        Restriction.ANIMAL_DERIVED, Restriction.LACTOSE
        }

    # Teste para um ingrediente com restrições desconhecidas
    ingredient3 = Ingredient("ingrediente_desconhecido")
    assert ingredient3.restrictions == set()
    assert repr(ingredient3) == "Ingredient('ingrediente_desconhecido')"

    # Teste para igualdade entre ingredientes
    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient_test
    assert hash(ingredient1) == hash(ingredient)
    assert hash(ingredient3) != hash(ingredient)
