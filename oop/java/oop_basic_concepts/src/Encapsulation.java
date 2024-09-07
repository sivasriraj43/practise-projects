class Car {
    private String brand;
    private String model;

    Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public void displayInfo() {
        System.out.println("Car Brand: " + brand + ", Model: " + model);
    }
}

public class Encapsulation {
    public static void main(String[] args) {
        Car car1 = new Car("Honda", "Civic");
        car1.displayInfo();  // Output: Car Brand: Honda, Model: Civic

        car1.setBrand("Toyota");  // Using setter method to modify encapsulated data
        System.out.println("Updated Brand: " + car1.getBrand());  // Output: Updated Brand: Toyota
    }
}
