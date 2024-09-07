class MathOperations {
    // Method Overloading
    int add(int a, int b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Overloading {
    public static void main(String[] args) {
        MathOperations obj = new MathOperations();
        System.out.println("Sum of two numbers: " + obj.add(10, 20));        // Output: 30
        System.out.println("Sum of three numbers: " + obj.add(10, 20, 30));  // Output: 60
    }
}
