from typing import Protocol


class FlyBehavior(Protocol):
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior(Protocol):
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

class Squack(QuackBehavior):
    def quack(self):
        print("Squack")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")
