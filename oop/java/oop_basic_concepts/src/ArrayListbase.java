package src;
import java.util.ArrayList;

public class ArrayListbase {
    public static void main(String[] args) {
        // Creating an ArrayList of Strings
        ArrayListbase<String> list = new ArrayListbase<>();

        // Adding elements to the ArrayList
        list.add("Apple");
        list.add("Banana");
        list.add("Orange");

        // Displaying the ArrayList
        System.out.println("ArrayList: " + list);  // Output: ArrayList: [Apple, Banana, Orange]
    }
}

