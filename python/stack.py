

class stack:

	def __init__(self):
		
		self.top = None

	def push(self, value):
		if (self.top == None):
			self.top = node(value)
		else:
			current = node(value)
			current.prev = self.top
			self.top = current

	def pop(self):
		if(self.top == None):
			return
		else:
			self.top = self.top.prev

	def find(self,value):
		if(self.top.data == value):
			return True
		current = self.top
		while(current != None):
			if(current.prev.data == value):
				return True
			else:
				current = current.prev
		return False

	def printStack(self):

		current = self.top
		while(current != None):
			print(current.data)
			current = current.prev


class node:

	def __init__(self, value):
		self.data = value
		self.prev = None

x = stack()
x.push(1)
x.push(50)
x.push(40)
x.push(3)
x.push(2)
x.printStack()

print(x.find(3))