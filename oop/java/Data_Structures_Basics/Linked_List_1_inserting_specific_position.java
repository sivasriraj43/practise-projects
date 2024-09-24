impor
class SinglyLinkedList {

    Node head;

    // Insert at a specific position (0-based index)
    void insertAtPosition(int data, int position) {
        Node newNode = new Node(data);

        if (position == 0) {
            newNode.next = head;
            head = newNode;
            return;
        }

        Node temp = head;
        for (int i = 0; temp != null && i < position - 1; i++) {
            temp = temp.next;
        }

        if (temp == null) {
            System.out.println("Position out of bounds");
            return;
        }

        newNode.next = temp.next;
        temp.next = newNode;
    }

    // Other methods (insertAtBeginning, insertAtEnd, display)...
}

public class Main {
    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);

        // Insert at position 1 (0-based index)
        list.insertAtPosition(15, 1);
        
        // Insert at the beginning
        list.insertAtPosition(5, 0);

        // Display the list
        list.display();  // Output: 5 -> 10 -> 15 -> 20 -> 30 -> null
    }
}
