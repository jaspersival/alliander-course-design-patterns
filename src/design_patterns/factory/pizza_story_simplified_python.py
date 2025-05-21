from design_patterns.factory.pizza import (
    NYStyleCheesePizza,
    NYStyleVeggiePizza,
    ChicagoStyleCheesePizza,
    ChicagoStyleVeggiePizza,
    Pizza,
)


class PizzaStoreSimple:
    # Mapping styles to their pizza types using types as first-class objects.
    _pizzas = {
        "NY": {
            "cheese": NYStyleCheesePizza,
            "veggie": NYStyleVeggiePizza,
        },
        "Chicago": {
            "cheese": ChicagoStyleCheesePizza,
            "veggie": ChicagoStyleVeggiePizza,
        },
    }

    def __init__(self, style: str):
        if style not in self._pizzas:
            raise ValueError(f"Unknown style: {style}")
        self._pizza_mapping = self._pizzas[style]

    def order_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type not in self._pizza_mapping:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
        # Create pizza using the class stored in the mapping.
        pizza = self._pizza_mapping[pizza_type]()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


# Example usage.
if __name__ == "__main__":
    ny_store = PizzaStoreSimple("NY")
    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    chicago_store = PizzaStoreSimple("Chicago")
    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza.name}\n")
