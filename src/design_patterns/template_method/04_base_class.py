from abc import ABC, abstractmethod


class BaseClass(ABC):
    def template_method(self) -> None:
        self.base_operation_one()
        self.required_operations_one()
        self.base_operation_two()
        self.hook_one()
        self.required_operations_two()
        self.base_operation_three()
        self.hook_two()

    def base_operation_one(self) -> None:
        print("BaseClass says: I am doing the bulk of the work")

    def base_operation_two(self) -> None:
        print("BaseClass says: But I let subclasses override some operations")

    def base_operation_three(self) -> None:
        print("BaseClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations_one(self) -> None:
        pass

    @abstractmethod
    def required_operations_two(self) -> None:
        pass

    def hook_one(self) -> None:
        pass

    def hook_two(self) -> None:
        pass
