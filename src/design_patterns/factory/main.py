from design_patterns.factory.pizza_store import (
    NYStylePizzaStore,
    ChicagoStylePizzaStore,
)


def main():
    ny_store = NYStylePizzaStore()
    chicago_store = ChicagoStylePizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.name}\n")

    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.name}\n")


if __name__ == "__main__":
    main()
