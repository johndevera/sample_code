class twoStacks:

	def __init__(self, n):
		self.size = n
		self.arr = [None] * n #list of nones for size n
		self.top1 = -1
		self.top2 = self.size


	def push1(self, value):
		#there is at least one empty space
		#check if top1 is less than top2, that's less than half
		if(self.top1 < self.top2 - 1):
			self.top1 = self.top1 + 1 # add first element to space 0
			self.arr[self.top1] = value
		else:
			print("stack overflow")
			exit(1)

	def push2(self, value):
		#there is at least one empty space
		#check if top1 is less than top2, that's less than half
		if(self.top1 < self.top2 - 1):
			self.top2 = self.top2 - 1 # add first element to space 0
			self.arr[self.top1] = value
		else:
			print("stack overflow")
			exit(1)

	def pop1(self):
		if self.top1 >= 0:
			x = self.arr[self.top1]
			self.top1 = self.top1 -1
			return x
		else:
			print("Stack Underflow ")
			exit(1)

	def pop2(self):
		if self.top2 < self.size:
			x = self.arr[self.top2]
			self.top1 = self.top1 + 1
			return x
		else:
			print("Stack Underflow ")
			exit(1)

ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
 
print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))

