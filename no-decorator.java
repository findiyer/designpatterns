// Component interface
interface Pizza {
    String getDescription();
    double getCost();
}

// Concrete Component
class Margherita implements Pizza {
    @Override
    public String getDescription() {
        return "Margherita Pizza";
    }

    @Override
    public double getCost() {
        return 6.99;
    }
}

// Concrete Component
class Pepperoni implements Pizza {
    @Override
    public String getDescription() {
        return "Pepperoni Pizza";
    }

    @Override
    public double getCost() {
        return 8.99;
    }
}

// Concrete Component
class Hawaiian implements Pizza {
    @Override
    public String getDescription() {
        return "Hawaiian Pizza";
    }

    @Override
    public double getCost() {
        return 7.99;
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        Pizza margherita = new Margherita();
        System.out.println("Description: " + margherita.getDescription());
        System.out.println("Cost: $" + margherita.getCost());

        Pizza pepperoni = new Pepperoni();
        System.out.println("Description: " + pepperoni.getDescription());
        System.out.println("Cost: $" + pepperoni.getCost());

        Pizza hawaiian = new Hawaiian();
        System.out.println("Description: " + hawaiian.getDescription());
        System.out.println("Cost: $" + hawaiian.getCost());
    }
}

