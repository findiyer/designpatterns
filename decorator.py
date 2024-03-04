# Define the component interface
class TeslaCarInterface:
    def get_description(self):
        pass

    def cost(self):
        pass

# Concrete component classes
class ModelY(TeslaCarInterface):
    def get_description(self):
        return "Tesla Model Y"

    def cost(self):
        return 60000

class Cybertruck(TeslaCarInterface):
    def get_description(self):
        return "Tesla Cybertruck"

    def cost(self):
        return 70000

# Define decorator base class
class TeslaCarDecorator(TeslaCarInterface):
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def get_description(self):
        return self._vehicle.get_description()

    def cost(self):
        return self._vehicle.cost()

# Define decorators
class FSDDecorator(TeslaCarDecorator):
    def get_description(self):
        return super().get_description() + ", FSD"

    def cost(self):
        return super().cost() + 5000

class PremiumInteriorDecorator(TeslaCarDecorator):
    def get_description(self):
        return super().get_description() + ", Premium Interior"

    def cost(self):
        return super().cost() + 3000

# Client code
if __name__ == "__main__":
    model_y = ModelY()
    print("Model Y:", model_y.get_description())
    print("Total Cost:", model_y.cost())

    fsd_model_y = FSDDecorator(model_y)
    print("Model Y with FSD:", fsd_model_y.get_description())
    print("Total Cost:", fsd_model_y.cost())

    premium_interior_model_y = PremiumInteriorDecorator(fsd_model_y)
    print("Model Y with FSD and Premium Interior:", premium_interior_model_y.get_description())
    print("Total Cost:", premium_interior_model_y.cost())

    model_y = ModelY()
    print("ORIGINAL:", model_y.get_description())
    print("Total Cost:", model_y.cost())

    # Create Cybertruck
    cybertruck = Cybertruck()
    print("Cybertruck:", cybertruck.get_description())
    print("Total Cost:", cybertruck.cost())

    # Add Full Self-Driving to Cybertruck
    fsd_cybertruck = FSDDecorator(cybertruck)
    print("Cybertruck with FSD:", fsd_cybertruck.get_description())
    print("Total Cost:", fsd_cybertruck.cost())

    # Add Premium Interior to Cybertruck
    premium_interior_cybertruck = PremiumInteriorDecorator(cybertruck)
    print("Cybertruck with Premium Interior:", premium_interior_cybertruck.get_description())
    print("Total Cost:", premium_interior_cybertruck.cost())
