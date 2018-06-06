
class linkedlist:

	

	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, value): 
		if (self.head == None): #if head node is null, assign it a value and make that current node
			self.head = node(value)
			self.tail = self.head
			return
		current = self.tail
		current.next = node(value)
		self.tail = current.next

		# current = self.head
		# while(current.next != None):
		# 	current = current.next
		# current.next = node(value)


	def prepend(self, data):
		newHead = node(data)
		newHead.next = self.head #newHead.next is pointing to old head
		self.head = newHead #the newHead is now the new node

	def deleteWithValue(self, data): 
		if (self.head == None):
			return
		if (self.head.data == data):
			self.head = self.head.next
			return
		#when you find the current.next == data, you want to point instead to its next value, (current.next.next)	
		current = self.head
		while(current != self.tail.next):
			if(current.next.data == data):
				current.next = current.next.next
				return
			else:
				current = current.next

	def printList(self):

		current = self.head
		while(current != None):
			print(current.data)
			current = current.next


class node:

	def __init__(self, value):
		self.data = value
		self.next = None






x = linkedlist()
x.append(3)
x.append(30)
x.append(10)
x.append(50)
x.append(1030)
x.append(556)
x.deleteWithValue(10)
x.prepend(46)
x.printList()


