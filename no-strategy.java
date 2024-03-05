// Strategy interface
interface PaymentStrategy {
    void pay(double amount);
}

// Concrete Strategy
class CreditCardPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paying $" + amount + " with credit card.");
    }
}

// Concrete Strategy
class PayPalPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paying $" + amount + " with PayPal.");
    }
}

// Concrete Strategy
class CashPayment implements PaymentStrategy {
    @Override
    public void pay(double amount) {
        System.out.println("Paying $" + amount + " with cash.");
    }
}

// Context class
class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public ShoppingCart(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void pay(double amount) {
        paymentStrategy.pay(amount);
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        PaymentStrategy creditCardPayment = new CreditCardPayment();
        PaymentStrategy payPalPayment = new PayPalPayment();
        PaymentStrategy cashPayment = new CashPayment();

        ShoppingCart cart1 = new ShoppingCart(creditCardPayment);
        cart1.pay(100);

        cart1.setPaymentStrategy(payPalPayment);
        cart1.pay(50);

        cart1.setPaymentStrategy(cashPayment);
        cart1.pay(75);
    }
}

