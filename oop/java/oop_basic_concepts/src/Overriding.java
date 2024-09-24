class Animal {
    void makeSound() {
        System.out.println("Some generic sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Meow");
    }
}

public class Overriding {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();
        Animal myDog = new Dog();  // Polymorphism in action
        Animal myCat = new Cat();

        myAnimal.makeSound();  // Output: Some generic sound
        myDog.makeSound();     // Output: Bark
        myCat.makeSound();     // Output: Meow
    }
}
