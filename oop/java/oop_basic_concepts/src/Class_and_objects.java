
class Car {
    String brand;
    String model;

    Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    void displayInfo() {
        System.out.println("Car Brand: " + brand + ", Model: " + model);
    }
}

public class Class_and_objects {
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", "Corolla");
        car1.displayInfo();  // Output: Car Brand: Toyota, Model: Corolla
    }
}
