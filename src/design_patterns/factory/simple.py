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
    @staticmethod
    def order_pizza(pizza_type: str) -> Pizza:
        pizza = SimplePizzaFactory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
