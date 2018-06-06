class linkedlist:

	def __init__(self):
		
		self.head = None
		self.tail = None
		pass

	def add(self, value):
		if (self.head == None):
			self.tail = node(value)
			self.head = node(value)
			print(self.head.data)
			return
		current = self.tail
		current.next = node(value)
		self.tail = current.next
		print(current.next.data)


	def reverse():
		pass

class node:

	def __init__(self, value):
		self.data = value
		self.next = None



x = linkedlist()
x.add(5)
x.add(3)
x.add(2)