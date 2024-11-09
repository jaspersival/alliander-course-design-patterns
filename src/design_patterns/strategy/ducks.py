import abc

from design_patterns.strategy.behaviors import (
    FlyWithWings,
    Quack,
    MuteQuack,
    FlyNoWay,
    FlyBehavior,
    QuackBehavior,
)


class Duck(abc.ABC):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")

    @staticmethod
    @abc.abstractmethod
    def display():
        pass


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    @staticmethod
    def display():
        print("I'm a real Mallard duck")


class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    @staticmethod
    def display():
        print("I'm a rubber duck")


class RedheadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    @staticmethod
    def display():
        print("I'm a real Redhead duck")


class DecoyDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    @staticmethod
    def display():
        print("I'm a duck Decoy")


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    @staticmethod
    def display():
        print("I'm a model duck")
