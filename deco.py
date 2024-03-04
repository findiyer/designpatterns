from abc import ABC, abstractmethod

# Abstract class for Tesla car
class TeslaCar(ABC):
    def __init__(self):
        self.cost = 0
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

# Concrete implementations for different Tesla models
class ModelX(TeslaCar):
    def __init__(self):
        super().__init__()
        self.cost = 80000

    def get_cost(self):
        return self.cost

    def get_description(self):
        return "Tesla Model X"

class ModelY(TeslaCar):
    def __init__(self):
        super().__init__()
        self.cost = 60000

    def get_cost(self):
        return self.cost

    def get_description(self):
        return "Tesla Model Y"

class Model3(TeslaCar):
    def __init__(self):
        super().__init__()
        self.cost = 40000

    def get_cost(self):
        return self.cost

    def get_description(self):
        return "Tesla Model 3"

# Decorators for adding options
class OptionsDecorator(TeslaCar):
    def __init__(self, car):
        super().__init__()
        self.car = car

    def add_option(self, option):
        self.car.add_option(option)

    def get_cost(self):
        return self.car.get_cost()

    def get_description(self):
        return self.car.get_description()

class FSD(OptionsDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.cost = 10000
        self.add_option("Full Self-Driving")

    def get_cost(self):
        return self.car.get_cost() + self.cost

class PremiumInterior(OptionsDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.cost = 5000
        self.add_option("Premium Interior")

    def get_cost(self):
        return self.car.get_cost() + self.cost

class TowHitch(OptionsDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.cost = 1000
        self.add_option("Tow Hitch")

    def get_cost(self):
        return self.car.get_cost() + self.cost

class CustomWheels(OptionsDecorator):
    def __init__(self, car):
        super().__init__(car)
        self.cost = 2000
        self.add_option("Custom Wheels")

    def get_cost(self):
        return self.car.get_cost() + self.cost

# Client code
if __name__ == "__main__":
    model_x = ModelX()
    print(model_x.get_description())
    print("Base cost:", model_x.get_cost())

    model_x_with_options = FSD(PremiumInterior(TowHitch(model_x)))
    print(model_x_with_options.get_description())
    print("Total cost with options:", model_x_with_options.get_cost())
    print("Options:", model_x_with_options.options)

