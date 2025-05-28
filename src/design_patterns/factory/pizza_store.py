from abc import ABC, abstractmethod

from design_patterns.factory.pizza import (
    NYStyleCheesePizza,
    NYStyleVeggiePizza,
    ChicagoStyleCheesePizza,
    ChicagoStyleVeggiePizza,
    Pizza,
)


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        raise NotImplementedError("This method should be overridden by subclasses")


class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case "cheese":
                return NYStyleCheesePizza()
            case "veggie":
                return NYStyleVeggiePizza()
            case _:
                raise ValueError(f"Unknown pizza type: {pizza_type}")


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        match pizza_type:
            case "cheese":
                return ChicagoStyleCheesePizza()
            case "veggie":
                return ChicagoStyleVeggiePizza()
            case _:
                raise ValueError(f"Unknown pizza type: {pizza_type}")
