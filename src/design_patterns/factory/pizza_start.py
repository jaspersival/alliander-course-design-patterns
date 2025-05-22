from design_patterns.factory.pizza import Pizza


def order_pizza() -> Pizza:
    pizza = Pizza()
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza


# But we need more than one type of pizza.
# So we need to create an order_pizza function that determines the type of pizza to create when a type is passed to it.
class CheesePizza(Pizza): ...


class VeggiePizza(Pizza): ...


class GreekPizza(Pizza): ...


def order_pizza_parametrized(pizza_type: str) -> Pizza:
    pizza: Pizza
    match pizza_type:
        case "cheese":
            pizza = CheesePizza()
        case "veggie":
            pizza = VeggiePizza()
        case "greek":
            pizza = GreekPizza()
        case _:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza
