from abc import ABC, abstractmethod

# Component interface
class TeslaComponent(ABC):
    @abstractmethod
    def assemble(self):
        pass

# Leaf class
class LeafComponent(TeslaComponent):
    def __init__(self, name):
        self.name = name

    def assemble(self, parentName):
        print(f"Assembling {self.name} - Leaf of {parentName}")

# Composite class
class CompositeComponent(TeslaComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def assemble(self, parentName):
        if not parentName:
            print(f"Assembling {self.name} - Composite")
        else:
            print(f"Assembling {self.name} - Composite. Leaf of {parentName}")
        for child in self.children:
            child.assemble(self.name)

# Builder base class
class TeslaBuilder(ABC):
    def __init__(self):
        self.car = CompositeComponent("Tesla Car")

    def build_chassis(self):
        self.car.add(CompositeComponent("Chassis"))
        self.car.children[0].add(LeafComponent("Suspension"))
        self.car.children[0].add(LeafComponent("Frame"))

    def build_electrical_system(self):
        self.car.add(CompositeComponent("Electrical System"))
        self.car.children[1].add(LeafComponent("Battery Pack"))
        self.car.children[1].add(LeafComponent("Wiring Harness"))

    def build_drivetrain(self):
        self.car.add(CompositeComponent("Drivetrain"))
        self.car.children[2].add(LeafComponent("Motor"))
        self.car.children[2].add(LeafComponent("Transmission"))

    def build_exterior_components(self):
        self.car.add(CompositeComponent("Exterior Components"))
        self.car.children[3].add(LeafComponent("Body Panels"))
        self.car.children[3].add(LeafComponent("Lights"))

    def build_interior_components(self):
        self.car.add(CompositeComponent("Interior Components"))
        self.car.children[4].add(LeafComponent("Dashboard"))
        self.car.children[4].add(LeafComponent("Seats"))
        infotainment_system = CompositeComponent("Infotainment System")
        infotainment_system.add(LeafComponent("Touchscreen"))
        self.car.children[4].add(infotainment_system)

    @abstractmethod
    def build_advanced_features(self):
        pass

    def get_result(self):
        return self.car

# Concrete builder for base car
class BaseTeslaBuilder(TeslaBuilder):
    def build_advanced_features(self):
        pass

# Concrete builder for premium car
class PremiumTeslaBuilder(TeslaBuilder):
    def build_advanced_features(self):
        advanced_features = CompositeComponent("Advanced Features")
        advanced_features.add(LeafComponent("Autopilot"))
        advanced_features.add(LeafComponent("Full Self-Driving Capability"))
        self.car.children[4].add(advanced_features)

# Director class
class TeslaAssemblyDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.build_chassis()
        self.builder.build_electrical_system()
        self.builder.build_drivetrain()
        self.builder.build_exterior_components()
        self.builder.build_interior_components()
        self.builder.build_advanced_features()

# Client code
if __name__ == "__main__":
    # Create base car builder
    base_builder = BaseTeslaBuilder()
    base_director = TeslaAssemblyDirector(base_builder)
    base_director.construct_car()
    base_car = base_builder.get_result()

    # Create premium car builder
    premium_builder = PremiumTeslaBuilder()
    premium_director = TeslaAssemblyDirector(premium_builder)
    premium_director.construct_car()
    premium_car = premium_builder.get_result()

    # Assemble base car
    print("Assembling Base Tesla Car:")
    base_car.assemble("")

    # Assemble premium car
    print("\nAssembling Premium Tesla Car:")
    premium_car.assemble("")
