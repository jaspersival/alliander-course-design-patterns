from design_patterns.factory.pizza_start import (
    Pizza,
    CheesePizza,
    VeggiePizza,
    GreekPizza,
    PepperoniPizza,
    ClamPizza,
)


class SimplePizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        pizza: Pizza
        match pizza_type:
            case "cheese":
                pizza = CheesePizza()
            case "veggie":
                pizza = VeggiePizza()
            case "greek":
                pizza = GreekPizza()
            case "pepperoni":
                pizza = PepperoniPizza()
            case "clam":
                pizza = ClamPizza()
            case _:
                raise ValueError(f"Unknown pizza type: {pizza_type}")
        return pizza


class PizzaStore:
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaFactory(SimplePizzaFactory): ...


class ChicagoPizzaFactory(SimplePizzaFactory): ...


if __name__ == "__main__":
    ny_factory = NYPizzaFactory()
    ny_store = PizzaStore(ny_factory)
    ny_store.order_pizza("cheese")

    chicago_factory = ChicagoPizzaFactory()
    chicago_store = PizzaStore(chicago_factory)
    chicago_store.order_pizza("cheese")
