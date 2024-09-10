class Node{
    int data;
    Node next;

    Node(int data){
        this.data =data;
        this.next = null;
    }
}

class LinkedList{
    Node head;

    void insert(int data){
        Node newNode = new Node(data);
        newNode.next = head;
        head= newNode;
    }

    void display(){
        Node current = head;
        while(current != null){
            System.out.print(current.data +" ");
            current =current.next;
        }
    }
}

public class Linked_List{
    public static void main(String[] args){
        LinkedList list = new LinkedList();
        list.insert(3);
        list.insert(2);
        list.insert(1);
        list.display();
    }
}