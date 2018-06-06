

class node:



	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, value):
		#check to see if bigger than left node. Recurssive
		if (value <= self.data):
			if(self.left == None):
				self.left = node(value)
			else:
				self.left.insert(value)
		else:
			if(self.right == None):
				self.right = node(value)
			else:
				self.right.insert(value)

	def contains(self, value):
		if (value < self.data):
			if(self.left == None):
				return False
			else:
				self.left.contains(value)
		else:
			if (self.right == None):
				return False
			else:
				self.right.contains(value)

	def printPreOrder(self):
		print(self.data)
		if(self.left != None):
			self.left.printPreOrder()
		if(self.right != None):
			self.right.printPreOrder()


	def printInOrder(self):
		if(self.left != None):
			self.left.printInOrder()
		print(self.data)
		if(self.right != None):
			self.right.printInOrder()

	def printPostOrder(self):
		if(self.left != None):
			self.left.printPostOrder()
		if(self.right != None):
			self.right.printPostOrder()
		print(self.data)





root = node(10)
root.insert(30)
root.insert(8)
root.insert(12)
root.insert(15)
root.insert(1)
root.insert(300)

root.printPostOrder()




