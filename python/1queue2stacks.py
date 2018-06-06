
class queue:

	def __init__(self):
		self.inStack = stack()
		self.outStack = stack()


	def enqueue(self, value):
		self.inStack.push(value)

	def dequeue(self):
		if (self.outStack.isEmpty()):
			while(!self.inStack.isEmpty):
				temp = self.inStack.pop()
				self.outStack.push()

		return self.outStack.pop()