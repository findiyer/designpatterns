// Strategy interface
interface BookingStrategy {
    void book(String roomType);
    void cancelBooking(String roomType);
}

// Concrete strategies
class OnlineBookingStrategy implements BookingStrategy {
    public void book(String roomType) {
        System.out.println("Booked " + roomType + " room online.");
    }

    public void cancelBooking(String roomType) {
        System.out.println("Canceled " + roomType + " room booking online.");
    }
}

class WalkInBookingStrategy implements BookingStrategy {
    public void book(String roomType) {
        System.out.println("Booked " + roomType + " room through walk-in.");
    }

    public void cancelBooking(String roomType) {
        System.out.println("Canceled " + roomType + " room booking through walk-in.");
    }
}

class OTABookingStrategy implements BookingStrategy {
    public void book(String roomType) {
        System.out.println("Booked " + roomType + " room through OTA.");
    }

    public void cancelBooking(String roomType) {
        System.out.println("Canceled " + roomType + " room booking through OTA.");
    }
}

// Context
class HotelBookingSystem {
    private BookingStrategy bookingStrategy;

    public HotelBookingSystem(BookingStrategy bookingStrategy) {
        this.bookingStrategy = bookingStrategy;
    }

    public void setBookingStrategy(BookingStrategy bookingStrategy) {
        this.bookingStrategy = bookingStrategy;
    }

    public void bookRoom(String roomType) {
        bookingStrategy.book(roomType);
    }

    public void cancelRoomBooking(String roomType) {
        bookingStrategy.cancelBooking(roomType);
    }
}

// Client code
class BookingEngine {
    public static void main(String[] args) {
        // Client can dynamically choose booking method
        BookingStrategy onlineBookingStrategy = new OnlineBookingStrategy();
        BookingStrategy walkInBookingStrategy = new WalkInBookingStrategy();
        BookingStrategy otaBookingStrategy = new OTABookingStrategy();

        HotelBookingSystem hotelSystem = new HotelBookingSystem(onlineBookingStrategy);
        hotelSystem.bookRoom("Standard");
        hotelSystem.cancelRoomBooking("Standard");

        hotelSystem.setBookingStrategy(walkInBookingStrategy);
        hotelSystem.bookRoom("Deluxe");
        hotelSystem.cancelRoomBooking("Deluxe");

        hotelSystem.setBookingStrategy(otaBookingStrategy);
        hotelSystem.bookRoom("Suite");
        hotelSystem.cancelRoomBooking("Suite");
    }
}

