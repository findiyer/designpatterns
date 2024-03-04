import copy

# Define the IVehicle interface
class IVehicle:
    def __str__(self):
        pass

    def clone(self):
        pass

# Define the TeslaVehicle class as the prototype
class TeslaVehicle(IVehicle):
    def __init__(self):
        self.model = ""
        self.color = ""
        self.engine_type = ""
        self.range = ""

    def __str__(self):
        return f"Tesla Vehicle: Model - {self.model}, Color - {self.color}, Engine Type - {self.engine_type}, Range - {self.range}"

    def clone(self):
        return copy.deepcopy(self)

# Define the concrete prototype classes for Tesla vehicles
class TeslaSUV(TeslaVehicle):
    def __init__(self):
        super().__init__()
        self.model = "Model X"
        self.range = "300 miles"

class TeslaSmallCar(TeslaVehicle):
    def __init__(self):
        super().__init__()
        self.model = "Model 3"
        self.range = "250 miles"

class TeslaSemi(TeslaVehicle):
    def __init__(self):
        super().__init__()
        self.model = "Semi"
        self.range = "500 miles"

class TeslaLuxuryCar(TeslaVehicle):
    def __init__(self):
        super().__init__()
        self.model = "Model S"
        self.range = "350 miles"

# Main code
if __name__ == "__main__":
    suv_prototype = TeslaSUV()
    small_car_prototype = TeslaSmallCar()
    semi_prototype = TeslaSemi()
    luxury_car_prototype = TeslaLuxuryCar()

    # Clone prototypes to create new instances
    suv = suv_prototype.clone()
    suv.color = "Black"
    print(suv)

    small_car = small_car_prototype.clone()
    small_car.color = "White"
    print(small_car)

    semi = semi_prototype.clone()
    semi.color = "Silver"
    print(semi)

    luxury_car = luxury_car_prototype.clone()
    luxury_car.color = "Red"
    print(luxury_car)

