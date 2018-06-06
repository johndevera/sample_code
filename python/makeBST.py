class node:

	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None


class BST:

	def __init__(self, myList):
		self.theList = myList
		self.theList = theList.mergeSort()
		self.home = node(None)
		self.theList.makeTree()

	def makeTree(self):
		root = int(self.theList / 2) # cast to int in case odd size in list
		if (root not in theList):
			root = node(root + 1)


		LHS, RHS = self.theList.split(root)
		if (!LHS.isEmpty()):
			LHS.makeTree()
		if (!RHS.isEmpty()):
			RHS.makeTree()



