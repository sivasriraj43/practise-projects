class SinglyLinkedList {

    Node head;

    // Reverse the linked list
    void reverse() {
        Node prev = null;
        Node current = head;
        Node next = null;

        while (current != null) {
            next = current.next;   // Store next node
            current.next = prev;   // Reverse the current node's pointer
            prev = current;        // Move the prev pointer ahead
            current = next;        // Move the current pointer ahead
        }

        head = prev;  // Update head to point to the last node
    }

    // Other methods (insertAtBeginning, insertAtEnd, display)...
}

public class Linked_List_3_reverse_linkedlist {
    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);

        System.out.println("Original List:");
        list.display();  // Output: 10 -> 20 -> 30 -> null

        list.reverse();

        System.out.println("Reversed List:");
        list.display();  // Output: 30 -> 20 -> 10 -> null
    }
}
