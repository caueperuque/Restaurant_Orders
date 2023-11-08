from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()

        with open(self.source_path) as file:
            file_reader = csv.DictReader(file, delimiter=",")
            data = file_reader
            for item in data:
                dish = Dish(item["dish"], float(item["price"]))
                ingredient = Ingredient(item["ingredient"])
                amount = item["recipe_amount"]

                if dish not in self.dishes:
                    dish.add_ingredient_dependency(ingredient, int(amount))
                    self.dishes.add(dish)
                    print(self.dishes)
                else:
                    for exist_dish in self.dishes:
                        if exist_dish.name == item["dish"]:
                            exist_dish.add_ingredient_dependency(
                                ingredient, int(amount)
                            )
