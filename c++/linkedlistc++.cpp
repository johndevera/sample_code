#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;

struct node{
	int data;
	node *next;
};

class list{
	private:
		node *head;
		node *tail;
	public:
		list(){
			head=NULL;
			tail=NULL;
		}

		void createNode(int value){
			node *temp = new node;
			temp->data = value;
			temp->next = NULL;
			if (head == NULL){
				head = temp;
				tail = temp;
				temp = NULL;
			}
			else{
				tail->next = temp;
				tail = temp;
			}
		}

		void display(){
			node *temp = new node;
			temp = head;
			while(temp != NULL){
				cout << temp->data << "\t";
				temp = temp->next;
			}
		}
		void instertAtStart(int value){
			node *temp = new node;
			temp->data = value;
			temp->next = head;
			head = temp;
		}
		void insertAtEnd(int value){
			node *temp = new node;
			temp->data = value;
			temp->next = NULL;
			tail->next = temp;
			tail = temp;
		}

		void insertAtPosition(int pos, int value){
			node *pre = new node;
			node *cur = new node;
			node *temp = new node;
			cur = head;
			for (int i =1; i < pos; i++){
				pre = cur;
				cur = cur->next;
			}
			temp->data = value;
			pre->next = temp;
			temp->next = cur; 
		}

};


int main(void){

list x;
x.createNode(10);
x.createNode(20);
x.createNode(30);
x.insertAtPosition(3, 25);
x.display();


return 0;
}


