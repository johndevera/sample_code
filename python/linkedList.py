class LinkedList:

	count = 0

	def __init__(self):
		self.next = None
		self.nodeCount = LinkedList.count + 1
		LinkedList.count += 1

	def add(self, node):
		self.next = node
	
	def printNode(self):
		print(self.nodeCount)
		return self.next

def reverse(root):
	
	if(root == None):
		return

	previous = None
	current = root
	nextNode = current.next

	while(nextNode != None):
		   
		current.next = previous
		previous = current
		current = nextNode
		nextNode = current.next


	return previous

one = LinkedList()
two = LinkedList()
three = LinkedList()
four = LinkedList()
five = LinkedList()

LinkedList.add(one, two)
LinkedList.add(two, three)
LinkedList.add(three, four)
LinkedList.add(four, five)

x = reverse(one)

x1 = x.printNode()
x2 = x1.printNode()
x3 = x2.printNode()
x4 = x3.printNode()



