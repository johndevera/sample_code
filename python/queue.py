class q: #queue

	def __init__(self):
		self.front = None
		self.back = None

	def enqueue(self, value): #join the line at the back
		#check if front is empty
		newVal = node(value)
		if (self.back == None): # if first in the queue
			self.front = newVal
			self.back = self.front
		else:
			self.back.behind = newVal
			newVal.forward = self.back
			self.back = newVal


	def dequeue(self): #leave the line from the front
		if(self.front == None):
			return None
		else: #there something there
			newVal = self.front #this value will be removed from queue
			self.front = self.front.behind #update the front to be the front's behind node
			return newVal


	def printQueue(self):
		current = self.front
		while(current != None):
			print(current.data)
			current = current.behind


class node:

	def __init__(self, value):

		self.data = value
		self.forward = None
		self.behind = None


x = q()
x.enqueue(1)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
x.enqueue(6)
x.enqueue(20)
x.enqueue(2)
x.enqueue(10)
x.enqueue(12)
x.dequeue()
x.printQueue()



