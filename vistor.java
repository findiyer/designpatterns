import java.util.ArrayList;
import java.util.List;

// Element interface
interface ReservationElement {
    void accept(ReservationVisitor visitor);
}

// Concrete Element
class CashReservation implements ReservationElement {
    private double amount;

    public CashReservation(double amount) {
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }

    @Override
    public void accept(ReservationVisitor visitor) {
        visitor.visit(this);
    }
}

// Concrete Element
class PointsReservation implements ReservationElement {
    private int points;

    public PointsReservation(int points) {
        this.points = points;
    }

    public int getPoints() {
        return points;
    }

    @Override
    public void accept(ReservationVisitor visitor) {
        visitor.visit(this);
    }
}

// Concrete Element
class PointsPlusCashReservation implements ReservationElement {
    private int points;
    private double cashAmount;

    public PointsPlusCashReservation(int points, double cashAmount) {
        this.points = points;
        this.cashAmount = cashAmount;
    }

    public int getPoints() {
        return points;
    }

    public double getCashAmount() {
        return cashAmount;
    }

    @Override
    public void accept(ReservationVisitor visitor) {
        visitor.visit(this);
    }
}

// Visitor interface
interface ReservationVisitor {
    void visit(CashReservation reservation);
    void visit(PointsReservation reservation);
    void visit(PointsPlusCashReservation reservation);
}

// Concrete Visitor
class TotalCalculator implements ReservationVisitor {
    @Override
    public void visit(CashReservation reservation) {
        System.out.println("Total Cash for this reservation: " + reservation.getAmount());
    }

    @Override
    public void visit(PointsReservation reservation) {
        System.out.println("Total Points for this reservation: " + reservation.getPoints());
    }

    @Override
    public void visit(PointsPlusCashReservation reservation) {
        System.out.printf("Total for this reservation: Cash %.2f + Points %d", reservation.getCashAmount(), reservation.getPoints());
    }
}

class Visitor {
    public static void main(String[] args) {
        List<ReservationElement> reservations = new ArrayList<>();
        reservations.add(new CashReservation(50.0));
        reservations.add(new PointsReservation(175));
        reservations.add(new PointsPlusCashReservation(100, 25.0));

        ReservationVisitor visitor = new TotalCalculator();

        for (ReservationElement reservation : reservations) {
            reservation.accept(visitor);
        }
    }
}

