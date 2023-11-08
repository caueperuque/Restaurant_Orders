import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    # Teste para um prato com o construtor correto
    dish1 = Dish("Risoto de Camarão", 65.00)
    dish2 = Dish("Risoto de Camarão", 65.00)
    dish3 = Dish("pizza de strogonoff", 47.00)
    assert dish1.name == "Risoto de Camarão"
    assert dish1.price == 65.00

    # Teste para um prato com o construtor incorreto
    with pytest.raises(TypeError) as excinfo:
        Dish("Prato inválido", "Preço inválido")
    assert str(excinfo.value) == "Dish price must be float."

    with pytest.raises(ValueError) as excinfo:
        Dish("Prato com preço inválido", 0)
    assert str(excinfo.value) == "Dish price must be greater then zero."

    # Teste para adicionar ingrediente corretamente
    ingredient1 = Ingredient("camarão")
    ingredient2 = Ingredient("queijo mussarela")
    dish1.add_ingredient_dependency(ingredient1, 10)
    dish1.add_ingredient_dependency(ingredient2, 1)
    assert dish1.recipe == {ingredient1: 10, ingredient2: 1}

    # Teste para verificar igualdade entre os pratos
    assert dish1 == dish2
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Teste para verificar se todos os ingredientes estão corretos
    assert dish1.get_ingredients() == {ingredient1, ingredient2}

    # Teste para verificar o retorno da Classe
    assert repr(dish1) == "Dish('Risoto de Camarão', R$65.00)"

    # Teste para verificar as restrictions
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }
