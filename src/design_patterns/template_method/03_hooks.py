from abc import ABC, abstractmethod


class CaffeineBeverageWithHook(ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()

        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self) -> None:
        raise NotImplementedError

    def boil_water(self) -> None:
        print("Boiling water")

    def pour_in_cup(self) -> None:
        print("Pouring into cup")

    def customer_wants_condiments(self) -> bool:
        return True


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Steeping the tea")

    def add_condiments(self) -> None:
        print("Adding Lemon")

    def customer_wants_condiments(self) -> bool:
        answer = self._get_user_input()
        return answer.startswith("y")

    def _get_user_input(self) -> str:
        try:
            answer = input("Would you like lemon with your tea (y/n)?").strip().lower()
            return answer if answer else "no"
        except IOError:
            print("IO error trying to read your answer")
            return "n"


class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self) -> None:
        print("Dripping Coffee through filter")

    def add_condiments(self) -> None:
        print("Adding Sugar and Milk")

    def customer_wants_condiments(self) -> bool:
        answer = self._get_user_input()
        return answer.startswith("y")

    def _get_user_input(self) -> str:
        try:
            answer = (
                input("Would you like milk and sugar with your coffee (y/n)?")
                .strip()
                .lower()
            )
            return answer if answer else "no"
        except IOError:
            print("IO error trying to read your answer")
            return "n"


def caffeine_beverage_with_hook_test_drive():
    tea_with_hook = TeaWithHook()
    coffee_with_hook = CoffeeWithHook()

    print("\nMaking tea...")
    tea_with_hook.prepare_recipe()

    print("\nMaking coffee...")
    coffee_with_hook.prepare_recipe()


if __name__ == "__main__":
    caffeine_beverage_with_hook_test_drive()
