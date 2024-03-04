class IVehicle:
    def get_model(self):
        pass

    def get_color(self):
        pass

    def get_engine_type(self):
        pass

    def get_range(self):
        pass

class TeslaSUV(IVehicle):
    def __init__(self, color):
        self.model = "Model X"
        self.color = color
        self.engine_type = "Electric"
        self.range = "300 miles"

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_engine_type(self):
        return self.engine_type

    def get_range(self):
        return self.range

class TeslaSmallCar(IVehicle):
    def __init__(self, color):
        self.model = "Model 3"
        self.color = color
        self.engine_type = "Electric"
        self.range = "250 miles"

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_engine_type(self):
        return self.engine_type

    def get_range(self):
        return self.range

class TeslaSemi(IVehicle):
    def __init__(self, color):
        self.model = "Semi"
        self.color = color
        self.engine_type = "Electric"
        self.range = "500 miles"

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_engine_type(self):
        return self.engine_type

    def get_range(self):
        return self.range

class TeslaLuxuryCar(IVehicle):
    def __init__(self, color):
        self.model = "Model S"
        self.color = color
        self.engine_type = "Electric"
        self.range = "350 miles"

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_engine_type(self):
        return self.engine_type

    def get_range(self):
        return self.range

class TeslaFactory:
    def create_vehicle(self, vehicle_type, color):
        if vehicle_type.lower() == "suv":
            return TeslaSUV(color)
        elif vehicle_type.lower() == "small car":
            return TeslaSmallCar(color)
        elif vehicle_type.lower() == "semi":
            return TeslaSemi(color)
        elif vehicle_type.lower() == "luxury car":
            return TeslaLuxuryCar(color)
        else:
            raise ValueError("Invalid vehicle type")

if __name__ == "__main__":
    tesla_factory = TeslaFactory()
    
    # Create SUV
    suv = tesla_factory.create_vehicle("SUV", "Black")
    print(f"{suv.get_model()} - Color: {suv.get_color()}, Engine Type: {suv.get_engine_type()}, Range: {suv.get_range()}")

    # Create Small Car
    small_car = tesla_factory.create_vehicle("Small Car", "White")
    print(f"{small_car.get_model()} - Color: {small_car.get_color()}, Engine Type: {small_car.get_engine_type()}, Range: {small_car.get_range()}")

    # Create Semi
    semi = tesla_factory.create_vehicle("Semi", "Silver")
    print(f"{semi.get_model()} - Color: {semi.get_color()}, Engine Type: {semi.get_engine_type()}, Range: {semi.get_range()}")

