
class Node{
    /**
        @param {Number} valuer
        @param {Node | null} next 
    */
    constructor(value){
        this.value = value;
        this.next = null; 
    }
}

class linkedList{
    constructor(){
        this.head = null
    }

    /**
        @param {Number} target
    */
    insertionAtEnd(target){
        if(this.head == null){
            let newNode = new Node(target); 
            this.head = newNode; 
        }
        let n = this.head
        while(n.next != null){
            n = n.next
        }
        let newNode = new Node(target); 
        n.next = newNode
    }
    display(){
        if(this.head == null){
            return; 
        }
        let n = this.head
        while(n != null){
            console.log(`${n.value}=>`)
            n = n.next
        }
    }
}

let ele = [1, 2, 3, 4, 5]
let fu = new linkedList();
for(let i = 0; i < ele.length; i++){
    fu.insertionAtEnd(ele[i])
}
fu.display(); 
