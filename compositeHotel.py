

from abc import ABC, abstractmethod

# Component interface
class RoomComponent(ABC):
    @abstractmethod
    def display(self):
        pass

# Leaf class
class SingleRoom(RoomComponent):
    def __init__(self, room_number):
        self.room_number = room_number

    def display(self):
        print(f"Single Room: {self.room_number}")

# Composite class
class CompositeRoom(RoomComponent):
    def __init__(self, room_number):
        self.room_number = room_number
        self.children = []

    def add(self, room):
        if room not in self.children:
            self.children.append(room)
        else:
            print(f"Room {room.room_number} already added to Composite Room {self.room_number}")

    def remove(self, room):
        self.children.remove(room)

    def display(self):
        print(f"Composite Room: {self.room_number}. It contains following rooms:")
        for room in self.children:
            room.display()
        print(f"Composite Room: {self.room_number} END")
# Client code
if __name__ == "__main__":
    room101 = SingleRoom(101)
    room102 = SingleRoom(102)
    room103 = SingleRoom(103)

    group_room = CompositeRoom(10001)
    group_room.add(room101)
    group_room.add(room102)
    group_room.add(room103)

    connected_room = CompositeRoom(20001)
    room201 = SingleRoom(201)
    room202 = SingleRoom(202)
    connected_room.add(room201)
    connected_room.add(room202)

    room301 = SingleRoom(301)
    room302 = SingleRoom(302)
    hotel = CompositeRoom("Hotel")
    hotel.add(group_room)  # Adding composite node
    hotel.add(connected_room)  # Adding composite node
    hotel.add(room301)  # Adding leaf node
    hotel.add(room302)  # Adding leaf node

    hotel.display()

