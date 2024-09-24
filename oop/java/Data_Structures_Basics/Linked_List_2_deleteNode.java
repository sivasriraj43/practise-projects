class SinglyLinkedList{
    Node head;

    void deleteAtBeginning(){
        if(head == null){
            System.out.println("List is empty");
            return;
        }
        head = head.next;
    }

    void deleteAtEnd(){
        if (head ==null){
            System.out.println("List is empty");
            return;
        }
        if(head.next==null){
            head =null;
            return;
        }
        Node temp = head;
        while(temp.next.next != null){
            temp = temp.next;
        }
        temp.next = null;
    }

    void deleteAtPosition(int position){
        if (head == null){
            System.out.println("List is empty");
            return;

        }
        if (position ==0){
            head = head.next;
            return;
        }

        Node temp = head;
        for (int i=0;temp != null && i < position -1;i++){
            temp =temp.next;

        }

        if(temp == null || temp.next ==null){
            System.out.println("Position out of bounds");
            return;
        }

        temp.next = temp.next.next;
    }

}

public class Main {
    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);

        // Delete the first node
        list.deleteAtBeginning(); // Removes 10
        list.display();  // Output: 20 -> 30 -> 40 -> null

        // Delete the last node
        list.deleteAtEnd();  // Removes 40
        list.display();  // Output: 20 -> 30 -> null

        // Delete node at position 1
        list.deleteAtPosition(1);  // Removes 30
        list.display();  // Output: 20 -> null
    }
}
