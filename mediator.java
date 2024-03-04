import java.util.ArrayList;
import java.util.List;

// Mediator interface
interface HotelMediator {
    void bookRoom(Room room, Guest guest);
    void cancelBooking(Room room, Guest guest);
}

// Concrete Mediator
class Hotel implements HotelMediator {
    private List<Room> rooms;

    public Hotel() {
        this.rooms = new ArrayList<>();
    }

    public void addRoom(Room room) {
        rooms.add(room);
    }

    @Override
    public void bookRoom(Room room, Guest guest) {
        room.book(guest);
    }

    @Override
    public void cancelBooking(Room room, Guest guest) {
        room.cancelBooking(guest);
    }
}

// Colleague interface
abstract class Room {
    protected HotelMediator mediator;

    public Room(HotelMediator mediator) {
        this.mediator = mediator;
    }

    public abstract void book(Guest guest);
    public abstract void cancelBooking(Guest guest);
}

// Concrete Colleague
class StandardRoom extends Room {
    private String number;
    private boolean booked;
    private Guest guest;

    public StandardRoom(HotelMediator mediator, String number) {
        super(mediator);
        this.number = number;
        this.booked = false;
        this.guest = null;
    }

    @Override
    public void book(Guest guest) {
        if (!booked) {
            booked = true;
            this.guest = guest;
            System.out.println("Standard Room " + number + " has been booked by " + guest.getName());
        } else {
            System.out.println("Standard Room " + number + " is already booked.");
        }
    }

    @Override
    public void cancelBooking(Guest guest) {
        if (this.guest != null && this.guest.equals(guest)) {
            booked = false;
            this.guest = null;
            System.out.println("Booking for Standard Room " + number + " has been canceled by " + guest.getName());
        } else {
            System.out.println("Cannot cancel booking for Standard Room " + number + ". Guest does not match.");
        }
    }
}

// Concrete Colleague
class Guest {
    private String name;

    public Guest(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class Mediator {
    public static void main(String[] args) {
        HotelMediator mediator = new Hotel();
        Room room101 = new StandardRoom(mediator, "101");
        Room room102 = new StandardRoom(mediator, "102");

        ((Hotel) mediator).addRoom(room101);
        ((Hotel) mediator).addRoom(room102);

        Guest guest1 = new Guest("John");
        Guest guest2 = new Guest("Alice");

        mediator.bookRoom(room101, guest1);
        mediator.bookRoom(room101, guest2);

        mediator.cancelBooking(room101, guest2);
    }
}

