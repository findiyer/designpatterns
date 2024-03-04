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

# Client code
if __name__ == "__main__":
    # Create composite components
    chassis = CompositeComponent("Chassis")
    electrical_system = CompositeComponent("Electrical System")
    drivetrain = CompositeComponent("Drivetrain")
    exterior_components = CompositeComponent("Exterior Components")
    interior_components = CompositeComponent("Interior Components")
    advanced_features = CompositeComponent("Advanced Features")

    # Add leaf components to composite components
    chassis.add(LeafComponent("Suspension"))
    chassis.add(LeafComponent("Frame"))

    electrical_system.add(LeafComponent("Battery Pack"))
    electrical_system.add(LeafComponent("Wiring Harness"))

    drivetrain.add(LeafComponent("Motor"))
    drivetrain.add(LeafComponent("Transmission"))

    exterior_components.add(LeafComponent("Body Panels"))
    exterior_components.add(LeafComponent("Lights"))

    interior_components.add(LeafComponent("Dashboard"))
    interior_components.add(LeafComponent("Seats"))
    infotainment_system = CompositeComponent("Infotainment System")
    infotainment_system.add(LeafComponent("Touchscreen"))
    interior_components.add(infotainment_system)

    advanced_features.add(LeafComponent("Autopilot"))
    advanced_features.add(LeafComponent("Full Self-Driving Capability"))

    # Assemble the car
    assembly_line = CompositeComponent("Tesla Car Assembly ROOT")
    assembly_line.add(chassis)
    assembly_line.add(electrical_system)
    assembly_line.add(drivetrain)
    assembly_line.add(exterior_components)
    assembly_line.add(interior_components)
    assembly_line.add(advanced_features)

    # Start the assembly process
    assembly_line.assemble("")

