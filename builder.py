from abc import ABC, abstractmethod

# Define the IVehicle interface
class IVehicle:
    def __str__(self):
        pass

# Define the Tesla vehicle classes
class TeslaSUV(IVehicle):
    def __init__(self):
        self.model = ""
        self.color = ""
        self.engine_type = ""
        self.range = ""

    def __str__(self):
        return f"Tesla SUV: Model - {self.model}, Color - {self.color}, Engine Type - {self.engine_type}, Range - {self.range}"

class TeslaSmallCar(IVehicle):
    def __init__(self):
        self.model = ""
        self.color = ""
        self.engine_type = ""
        self.range = ""

    def __str__(self):
        return f"Tesla Small Car: Model - {self.model}, Color - {self.color}, Engine Type - {self.engine_type}, Range - {self.range}"

class TeslaSemi(IVehicle):
    def __init__(self):
        self.model = ""
        self.color = ""
        self.engine_type = ""
        self.range = ""

    def __str__(self):
        return f"Tesla Semi: Model - {self.model}, Color - {self.color}, Engine Type - {self.engine_type}, Range - {self.range}"

class TeslaLuxuryCar(IVehicle):
    def __init__(self):
        self.model = ""
        self.color = ""
        self.engine_type = ""
        self.range = ""

    def __str__(self):
        return f"Tesla Luxury Car: Model - {self.model}, Color - {self.color}, Engine Type - {self.engine_type}, Range - {self.range}"


# Define the builder interface
class TeslaBuilder(ABC):
    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    @abstractmethod
    def set_engine_type(self):
        pass

    @abstractmethod
    def set_range(self):
        pass

    @abstractmethod
    def get_vehicle(self):
        pass

# Concrete builder for Tesla SUV
class TeslaSUVBuilder(TeslaBuilder):
    def __init__(self):
        self.vehicle = TeslaSUV()

    def set_model(self):
        self.vehicle.model = "Model X"

    def set_color(self):
        self.vehicle.color = "white"

    def set_engine_type(self):
        self.vehicle.engine_type = "Electric"

    def set_range(self):
        self.vehicle.range = "300 miles"

    def get_vehicle(self):
        return self.vehicle

# Concrete builder for Tesla Small Car
class TeslaSmallCarBuilder(TeslaBuilder):
    def __init__(self):
        self.vehicle = TeslaSmallCar()

    def set_model(self):
        self.vehicle.model = "Model 3"

    def set_color(self):
        self.vehicle.color = "black"

    def set_engine_type(self):
        self.vehicle.engine_type = "Electric"

    def set_range(self):
        self.vehicle.range = "250 miles"

    def get_vehicle(self):
        return self.vehicle

# Concrete builder for Tesla Semi
class TeslaSemiBuilder(TeslaBuilder):
    def __init__(self):
        self.vehicle = TeslaSemi()

    def set_model(self):
        self.vehicle.model = "Semi"

    def set_color(self):
        self.vehicle.color = "red"

    def set_engine_type(self):
        self.vehicle.engine_type = "Electric"

    def set_range(self):
        self.vehicle.range = "500 miles"

    def get_vehicle(self):
        return self.vehicle

# Concrete builder for Tesla Luxury Car
class TeslaLuxuryCarBuilder(TeslaBuilder):
    def __init__(self):
        self.vehicle = TeslaLuxuryCar()

    def set_model(self):
        self.vehicle.model = "Model S"

    def set_color(self):
        self.vehicle.color = "silver"

    def set_engine_type(self):
        self.vehicle.engine_type = "Electric"

    def set_range(self):
        self.vehicle.range = "350 miles"

    def get_vehicle(self):
        return self.vehicle

# Define the director class for building vehicles
class TeslaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_vehicle(self):
        self.builder.set_model()
        self.builder.set_color()
        self.builder.set_engine_type()
        self.builder.set_range()

# Define the Tesla factory class
class TeslaFactory:
    def create_builder(self, vehicle_type):
        if vehicle_type.lower() == "suv":
            return TeslaSUVBuilder()
        elif vehicle_type.lower() == "small car":
            return TeslaSmallCarBuilder()
        elif vehicle_type.lower() == "semi":
            return TeslaSemiBuilder()
        elif vehicle_type.lower() == "luxury car":
            return TeslaLuxuryCarBuilder()
        else:
            raise ValueError("Invalid vehicle type")

# Main code
if __name__ == "__main__":
    factory = TeslaFactory()
    
    vehicle_types = ["SUV", "Small Car", "Semi"]
    for vehicle_type in vehicle_types:
        builder = factory.create_builder(vehicle_type)
        director = TeslaDirector(builder)
        director.construct_vehicle()  
        vehicle = builder.get_vehicle()
        print(vehicle)
