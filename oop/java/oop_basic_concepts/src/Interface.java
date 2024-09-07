interface Animal {
    // Interface method (does not have a body)
    void makeSound();
}

class Dog implements Animal {
    // Implementing interface method
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Interface {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound();  // Output: Bark
    }
}
