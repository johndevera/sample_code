


public class linkedlist{
	
	public linkedlist(){
		node head = null;
	}

	public void add(int value){
		linkedlist.head = new node(value);
		linkedlist.head.next = new node(null);
	}
	public static void main(String [] args){

	}
}


public class node{

	private int data;
	private node next;

	public node(int data){
		this.data = data;
		this.next = null;
	}
	
}