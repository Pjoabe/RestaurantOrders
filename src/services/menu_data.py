import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self._load_menu_data()

    def _load_menu_data(self) -> None:
        with open(self.source_path, "r", newline="") as csvfile:
            read = csv.reader(csvfile)
            next(read)
            for row in read:
                dish_name = row[0]
                cost = float(row[1])
                ingredient_name = row[2]
                ammount = int(row[3])
                ingredient = Ingredient(ingredient_name)
                dish = next(
                    (dish for dish in self.dishes if dish.name == dish_name),
                    None
                )
                if dish is None:
                    dish = Dish(dish_name, cost)
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, ammount)
