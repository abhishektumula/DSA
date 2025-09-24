class Node{
    int value;
    Node next; 
    
    public Node(int value){
        this.value = value; 
        this.next = null; 
    }
}

class linked{
    Node head; 
    public linked(){
        this.head = null; 
    }
    void insertionAtEnd(int target){
        if(this.head == null){
            Node newNode = new Node(target); 
            this.head = newNode; 
            return; 
        }else{
            Node n = this.head; 
            while(n.next != null){
                n = n.next; 
            }
            Node newNode = new Node(target); 
            n.next = newNode; 
            return; 
        } 
    }
    void insertionAtBegin(int target){
        if(this.head == null){
            Node newNode = new Node(target); 
            this.head = newNode; 
            return; 
        }else{
            Node newNode = new Node(target); 
            newNode.next = this.head; 
            this.head = newNode;
            return; 
        }
    }
    void deleteEnd(){
        if(this.head == null){
            return; 
        }
        Node n = this.head; 
        while(n.next.next != null){
            n = n.next; 
        }
        n.next = null; 
        return; 
    }
    void deleteStart(){
        if(this.head == null){
            return; 
        }else if(this.head.next == null){
            this.head = null; 
            return; 
        }
        Node newHead = this.head.next; 
        this.head.next = null; 
        this.head = newHead; 
        return; 
    }
    void display(){
        if(this.head == null){
            System.out.println("[empty list]");
            return; 
        }
        Node n = this.head; 
        while (n != null){
            System.out.print(n.value + "=>"); 
            n = n.next; 
        }
        System.out.println();
        return; 
    }
}

public class linkedList{
    public static void main(String [] args){
        int [] ele = {1, 2, 3, 4, 5}; 
        linked f1 = new linked(); 
        f1.display(); 
        for(int i = 0; i < ele.length; i++){
            f1.insertionAtEnd(ele[i]);
        }
        f1.insertionAtBegin(0);
        f1.display(); 
        f1.deleteEnd();
        f1.display(); 
        f1.deleteStart();
        f1.display(); 
    }
}
