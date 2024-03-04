# Define the component interface
class TeslaCarInterface:
    def get_description(self):
        pass

    def cost(self):
        pass

# Concrete component classes
class Cybertruck(TeslaCarInterface):
    def get_description(self):
        return "Cybertruck"

    def cost(self):
        return 50000  # Base cost of Cybertruck

class ModelY(TeslaCarInterface):
    def get_description(self):
        return "Model Y"

    def cost(self):
        return 4500  # Base cost of Model Y

# Define decorators
class FSDDecorator(TeslaCarInterface):
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def get_description(self):
        return self._vehicle.get_description() + ", Full Self-Driving (FSD)"

    def cost(self):
        return self._vehicle.cost() + 10000  # Additional cost for FSD

class PremiumInteriorDecorator(TeslaCarInterface):
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def get_description(self):
        return self._vehicle.get_description() + ", Premium Interior"

    def cost(self):
        return self._vehicle.cost() + 5000  # Additional cost for premium interior

# Factory class
class TeslaFactory:
    @staticmethod
    def create_decorated_vehicle(vehicle_type, fsd=False, premium_interior=False):
        if vehicle_type == "Cybertruck":
            vehicle = Cybertruck()
        elif vehicle_type == "Model Y":
            vehicle = ModelY()
        else:
            raise ValueError("Invalid vehicle type")

        if fsd:
            vehicle = FSDDecorator(vehicle)
        if premium_interior:
            vehicle = PremiumInteriorDecorator(vehicle)
        return vehicle

# Client code
if __name__ == "__main__":
    # Create base Cybertruck
    base_cybertruck = TeslaFactory.create_decorated_vehicle("Cybertruck")
    print("Base Cybertruck:", base_cybertruck.get_description())
    print("Total Cost:", base_cybertruck.cost())

    # Create Cybertruck with Full Self-Driving
    fsd_cybertruck = TeslaFactory.create_decorated_vehicle("Cybertruck", fsd=True)
    print("Cybertruck with Full Self-Driving:", fsd_cybertruck.get_description())
    print("Total Cost:", fsd_cybertruck.cost())

    # Create Cybertruck with Premium Interior
    premium_interior_cybertruck = TeslaFactory.create_decorated_vehicle("Cybertruck", premium_interior=True)
    print("Cybertruck with Premium Interior:", premium_interior_cybertruck.get_description())
    print("Total Cost:", premium_interior_cybertruck.cost())

    # Create Fully Featured Cybertruck
    full_featured_cybertruck = TeslaFactory.create_decorated_vehicle("Cybertruck", fsd=True, premium_interior=True)
    print("Fully Featured Cybertruck:", full_featured_cybertruck.get_description())
    print("Total Cost:", full_featured_cybertruck.cost())

    # Create base Model Y 
    base_model_y = TeslaFactory.create_decorated_vehicle("Model Y")
    print("Base Model Y:", base_model_y.get_description())
    print("Total Cost:", base_model_y.cost())

    # Create Model Y with Premium Interior
    premium_interior_model_y = TeslaFactory.create_decorated_vehicle("Model Y", premium_interior=True)
    print("Model Y with Premium Interior:", premium_interior_model_y.get_description())
    print("Total Cost:", premium_interior_model_y.cost())
