class SinglyLinkedList{

    Node head;

    void findMiddle(){
        if (head = null){
            System.out.println("List is empty");
            return;
        }
        Node slow = head;
        Node fast = head;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

        }
        System.out.println("Middle element: "+ slow.data);
    }
}

public class Linked_List_3_middle_linkedlist{
    public static void main(String[] args){
        SinglyLinkedList list = new SinglyLinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        list.insertAtEnd(50);

        list.display();;;;;;

        list.findMiddle(); 
    }
}