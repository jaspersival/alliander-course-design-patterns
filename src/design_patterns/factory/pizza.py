from abc import ABC


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: list[str] = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough: {self.dough}")
        print(f"Adding sauce: {self.sauce}")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f"  {topping}")

    @staticmethod
    def bake():
        print("Bake for 25 minutes at 350")

    @staticmethod
    def cut():
        print("Cutting the pizza into diagonal slices")

    @staticmethod
    def box():
        print("Place pizza in official PizzaStore box")


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")

    @staticmethod
    def cut():
        print("Cutting the pizza into square slices")


class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Veggie Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.extend(
            ["Grated Reggiano Cheese", "Black Olives", "Spinach", "Eggplant"]
        )


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.extend(
            ["Shredded Mozzarella Cheese", "Black Olives", "Spinach", "Eggplant"]
        )


class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Pepperoni Pizza"
        self.dough = "Regular Crust Dough"
        self.sauce = "Tomato Sauce"
        self.toppings.append("Sliced Pepperoni")


class ClamPizza(Pizza):
    def __init__(self):
        self.name = "Clam Pizza"
        self.dough = "Regular Crust Dough"
        self.sauce = "White Sauce"
        self.toppings.append("Fresh Clams")
