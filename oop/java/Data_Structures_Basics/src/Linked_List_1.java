<<<<<<< HEAD
class Node{
    int data;
    Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList{
    Node head;

    void insertAtBeggin(int data){
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;

    }

    void insertAtEnd(int data){
        Node newNode = new Node(data):
        if(head==null){
            head= newNode;
        } else{
            Node temp = head;
            while(temp.next !=null){
                temp = temp.next;
            }
            temp.next=newNode;
        }
        
    }

void display(){
    Node temp = head;
    while(temp != null){
        System.out.print(temp.data + "->");
        temp = temp.next;
    }
    System.out.println("null");
}
}

class Linked_List_1{
    public static void main(String[] args){
        SinglyLinkedList list = new SinglyLinkedList();

        //Inserting elements
        list.insertAtEnd(10);
        list.insertAtBeggin(5);
        list.insertAtEnd(20);
        list.insertAtBeggin(2);

        //Display the list
        list.display();
    }
}
=======
import java.util.LinkedList;

public class Linked_List_1{
	public static void main(String[] args) {
		LinkedList<String> list = new LinkedList<>();
		
		list.add("A");
		list.add("B");
		list.add("C");
		
		for (String i : list) {
			System.out.println(i);
			
		}
		
		list.remove("B");
		System.out.println("removed : "+list);
	}
}

//Dynamic size
//Efficient for insertions and deletions
//can be used to implement stacks,queues, etc

>>>>>>> e58eb147 (problem solving started)
