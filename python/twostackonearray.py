x = [10, 20, 30, 35, 4503, 430, 22, 3, 64]


class stack:

	stackSize = 0

	def __init__(self):
		self.myStack = []

	def frontPop(self):
		if len(self.myStack) == 0:
			print("Empty Stack")
			return 0
		pop = self.myStack[0]
		self.myStack.pop(0)
		return pop

	def frontPush(self, num):
		self.myStack.insert(0, num)

	def backPop(self):
		if len(self.myStack) == 0:
			print("Empty Stack")
			return 0
		end = len(self.myStack) - 1
		pop = self.myStack[end]
		self.myStack.pop(end)
		return pop

	def backPush(self, num):
		myStack.insert(0, num)



a = stack()

a.frontPush(1)
a.frontPush(2)
a.frontPush(3)
a.frontPush(4)
a.frontPush(5)

print(a.myStack)

print(a.frontPop(), "front")
print(a.backPop(), "wow")
print(a.frontPop(), "mee")

print(len(a.myStack))
