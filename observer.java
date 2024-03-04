import java.util.ArrayList;
import java.util.List;

// Subject interface
interface BookingSubject {
    void registerObserver(BookingObserver observer);
    void removeObserver(BookingObserver observer);
    void notifyObservers(String roomNumber, boolean isBooked);
}

// Concrete subject
class RoomBookingSystem implements BookingSubject {
    private List<BookingObserver> observers;
    private String roomNumber;
    private boolean isBooked;

    public RoomBookingSystem() {
        this.observers = new ArrayList<>();
    }

    @Override
    public void registerObserver(BookingObserver observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(BookingObserver observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(String roomNumber, boolean isBooked) {
        for (BookingObserver observer : observers) {
            observer.update(roomNumber, isBooked);
        }
    }

    public void setRoomStatus(String roomNumber, boolean isBooked) {
        // New line at the beginning
        System.out.println();
        this.roomNumber = roomNumber;
        this.isBooked = isBooked;
        if (isBooked) {
            System.out.println("Room " + roomNumber + " has been booked.");
        } else {
            System.out.println("Booking for room " + roomNumber + " has been canceled.");
        }
        notifyObservers(roomNumber, isBooked);
    }
}

// Observer interface
interface BookingObserver {
    void update(String roomNumber, boolean isBooked);
}

// Concrete observer (Loyalty program)
class LoyaltyProgram implements BookingObserver {
    @Override
    public void update(String roomNumber, boolean isBooked) {
        if (isBooked) {
            System.out.println("Loyalty Program: Earn points for booking room " + roomNumber);
        } else {
            System.out.println("Loyalty Program: Cancel points for canceled booking of room " + roomNumber);
        }
    }
}

// Concrete observer (Billing system)
class BillingSystem implements BookingObserver {
    @Override
    public void update(String roomNumber, boolean isBooked) {
        if (isBooked) {
            System.out.println("Billing System: Generate invoice for booking of room " + roomNumber);
        } else {
            System.out.println("Billing System: Void invoice for canceled booking of room " + roomNumber);
        }
    }
}

// Concrete observer (Customer notification system)
class CustomerNotificationSystem implements BookingObserver {
    @Override
    public void update(String roomNumber, boolean isBooked) {
        if (isBooked) {
            System.out.println("Customer Notification System: Send confirmation email for booking of room " + roomNumber);
        } else {
            System.out.println("Customer Notification System: Send cancellation email for canceled booking of room " + roomNumber);
        }
    }
}

// Client code
class HotelBookingSystem {
    public static void main(String[] args) {
        // Create subject (RoomBookingSystem)
        RoomBookingSystem roomBookingSystem = new RoomBookingSystem();

        // Create observers (LoyaltyProgram, BillingSystem, and CustomerNotificationSystem)
        LoyaltyProgram loyaltyProgram = new LoyaltyProgram();
        BillingSystem billingSystem = new BillingSystem();
        CustomerNotificationSystem customerNotificationSystem = new CustomerNotificationSystem();

        // Register observers with the subject
        roomBookingSystem.registerObserver(loyaltyProgram);
        roomBookingSystem.registerObserver(billingSystem);
        roomBookingSystem.registerObserver(customerNotificationSystem);

        // Simulate room booking events
        roomBookingSystem.setRoomStatus("101", true); // Book room 101
        roomBookingSystem.setRoomStatus("101", false); // Cancel booking for room 101
    }
}

