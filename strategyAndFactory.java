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

// Factory to decide which strategy to use
class BookingStrategyFactory {
    public static BookingStrategy createBookingStrategy(String bookingType) {
        switch (bookingType.toLowerCase()) {
            case "online":
                return new OnlineBookingStrategy();
            case "walk-in":
                return new WalkInBookingStrategy();
            case "ota":
                return new OTABookingStrategy();
            default:
                throw new IllegalArgumentException("Invalid booking type: " + bookingType);
        }
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
class strategyAndFactory {
    public static void main(String[] args) {
        // Create a hotel booking system with a default strategy
        HotelBookingSystem hotelSystem = new HotelBookingSystem(BookingStrategyFactory.createBookingStrategy("online"));

        // Book and cancel rooms using different strategies
        hotelSystem.bookRoom("Standard");
        hotelSystem.cancelRoomBooking("Standard");

        hotelSystem.setBookingStrategy(BookingStrategyFactory.createBookingStrategy("walk-in"));
        hotelSystem.bookRoom("Deluxe");
        hotelSystem.cancelRoomBooking("Deluxe");

        hotelSystem.setBookingStrategy(BookingStrategyFactory.createBookingStrategy("ota"));
        hotelSystem.bookRoom("Suite");
        hotelSystem.cancelRoomBooking("Suite");
    }
}

