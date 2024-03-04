from abc import ABC, abstractmethod

# Abstract Product A
class TeslaVehicle(ABC):
    @abstractmethod
    def __init__(self, model: str, range_: str, color: str):
        self.model = model
        self.range = range_
        self.color = color

    def __str__(self):
        return f"{self.model} - Color: {self.color}, Range: {self.range}"

# Concrete Product A1
class ModelX(TeslaVehicle):
    def __init__(self, color: str):
        super().__init__("Model X", "300 miles", color)

# Concrete Product A2
class ModelY(TeslaVehicle):
    def __init__(self, color: str):
        super().__init__("Model Y", "450 miles", color)

# Abstract Product B
class TeslaCharger(ABC):
    @abstractmethod
    def __init__(self, voltage: str, connector_type: str):
        self.voltage = voltage
        self.connector_type = connector_type

    def __str__(self):
        return f"Voltage: {self.voltage}, Connector Type: {self.connector_type}"

# Concrete Product B1
class LowVoltageCharger(TeslaCharger):
    def __init__(self):
        super().__init__("120V", "Type A")

# Concrete Product B2
class HighVoltageCharger(TeslaCharger):
    def __init__(self):
        super().__init__("240V", "Type B")

# Abstract Factory
class TeslaFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> TeslaVehicle:
        pass

    @abstractmethod
    def create_charger(self) -> TeslaCharger:
        pass

    @abstractmethod
    def region(self) -> str:
        pass

    def assemble_vehicle(self):
        vehicle = self.create_vehicle()
        charger = self.create_charger()
        print(f"Assemble Default Configuration in {self.region()} =  {vehicle} with {charger}.")

# Concrete Factory for North America
class NorthAmericaFactory(TeslaFactory):
    def __init__(self, car_type: str):
        self.car_type = car_type

    def create_vehicle(self) -> TeslaVehicle:
        if self.car_type.lower() == "suv":
            return ModelY("Black")
        elif self.car_type.lower() == "small":
            return ModelY("White")
        elif self.car_type.lower() == "luxury":
            return ModelX("Red")  # For demonstration, luxury car is Model X
        else:
            raise ValueError("Invalid car type")

    def create_charger(self) -> TeslaCharger:
        return LowVoltageCharger()  # Low voltage charger for North America

    def region(self) -> str:
        return "North America"

# Concrete Factory for Europe
class EuropeFactory(TeslaFactory):
    def __init__(self, car_type: str):
        self.car_type = car_type

    def create_vehicle(self) -> TeslaVehicle:
        if self.car_type.lower() == "suv":
            return ModelY("Blue")
        elif self.car_type.lower() == "small":
            return ModelY("Yellow")
        elif self.car_type.lower() == "luxury":
            return ModelX("Green")  # For demonstration, luxury car is Model Y
        else:
            raise ValueError("Invalid car type")

    def create_charger(self) -> TeslaCharger:
        return HighVoltageCharger()  # High voltage charger for Europe

    def region(self) -> str:
        return "Europe"

# Concrete Factory for Asia
class AsiaFactory(TeslaFactory):
    def __init__(self, car_type: str):
        self.car_type = car_type

    def create_vehicle(self) -> TeslaVehicle:
        if self.car_type.lower() == "suv":
            return ModelX("Silver")
        elif self.car_type.lower() == "small":
            return ModelX("Gray")
        elif self.car_type.lower() == "luxury":
            return ModelX("White")  # For demonstration, luxury car is Model X
        else:
            raise ValueError("Invalid car type")

    def create_charger(self) -> TeslaCharger:
        return HighVoltageCharger()  # High voltage charger for Asia

    def region(self) -> str:
        return "Asia"

# Client code
if __name__ == "__main__":
    na_factory = NorthAmericaFactory("SUV")
    eu_factory = EuropeFactory("Luxury")
    asia_factory = AsiaFactory("Small")

    na_factory.assemble_vehicle()
    eu_factory.assemble_vehicle()
    asia_factory.assemble_vehicle()

