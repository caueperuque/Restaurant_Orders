from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()

        with open(self.source_path) as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader
            for item in data:
                dish = Dish(item[0], float(item[1]))
                ingredient = Ingredient(item[2])
                amount = item[3]

                if dish not in self.dishes:
                    dish.add_ingredient_dependency(
                        ingredient, int(amount)
                    )
                    self.dishes.add(dish)
                else:
                    for exist_dish in self.dishes:
                        if exist_dish.name == item[0]:
                            exist_dish.add_ingredient_dependency(
                                ingredient, int(amount)
                            )
