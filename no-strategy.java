// Context class
class ShoppingCart {
    private String paymentMethod;

    public ShoppingCart(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public void pay(double amount) {
        if (paymentMethod.equalsIgnoreCase("credit card")) {
            System.out.println("Paying $" + amount + " with credit card.");
        } else if (paymentMethod.equalsIgnoreCase("paypal")) {
            System.out.println("Paying $" + amount + " with PayPal.");
        } else if (paymentMethod.equalsIgnoreCase("cash")) {
            System.out.println("Paying $" + amount + " with cash.");
        } else {
            System.out.println("Payment method not supported.");
        }
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        ShoppingCart cart1 = new ShoppingCart("credit card");
        cart1.pay(100);

        ShoppingCart cart2 = new ShoppingCart("paypal");
        cart2.pay(50);

        ShoppingCart cart3 = new ShoppingCart("cash");
        cart3.pay(75);

        ShoppingCart cart4 = new ShoppingCart("bitcoin"); // Unsupported payment method
        cart4.pay(200);
    }
}

