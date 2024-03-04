from abc import ABC, abstractmethod

# Adaptee: Tesla Car
class TeslaCar:
    def get_current_location(self):
        return {"latitude": 37.7749, "longitude": -122.4194}  # Example location data format from Tesla

# Target interface expected by the navigation system
class NavigationSystem(ABC):
    @abstractmethod
    def show_map(self, latitude, longitude):
        pass

# Adapter class to adapt TeslaCar to NavigationSystem interface
class TeslaNavigationAdapter(NavigationSystem):
    def __init__(self, tesla_car):
        self.tesla_car = tesla_car

    def show_map(self, latitude, longitude):
        location_data = self.tesla_car.get_current_location()
        latitude = location_data["latitude"]
        longitude = location_data["longitude"]
        print(f"Displaying map at Tesla car's location: Latitude {latitude}, Longitude {longitude}")

# Third-party navigation system that expects location data in latitude and longitude format
class ThirdPartyNavigationSystem(NavigationSystem):
    def show_map(self, latitude, longitude):
        print(f"Displaying map at coordinates: {latitude}, {longitude}")

# Client code
if __name__ == "__main__":
    # Create Tesla car instance
    tesla_car = TeslaCar()

    # Create adapter instance, passing Tesla car as parameter
    adapter = TeslaNavigationAdapter(tesla_car)

    # Create instance of the third-party navigation system
    navigation_system = ThirdPartyNavigationSystem()

    # Use the third-party navigation system with the adapted Tesla car
    adapter.show_map(0, 0)  # Adapter adapts Tesla car's location data to latitude and longitude
    latitude, longitude = 37.7749, -122.4194  # Example latitude and longitude
    navigation_system.show_map(latitude, longitude)  # Third-party navigation system expects latitude and longitude

