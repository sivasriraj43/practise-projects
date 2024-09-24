abstract class Animal {
    // Abstract method (does not have a body)
    abstract void makeSound();

    // Regular method
    void sleep() {
        System.out.println("Sleeping...");
    }
}

class Dog extends Animal {
    // Implementing abstract method
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

public class Abstract {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound();  // Output: Bark
        dog.sleep();      // Output: Sleeping...
    }
}
