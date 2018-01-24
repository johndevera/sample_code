#enqueue dequeue

class person:
	numInLine = 0
	def __init__(self):
		person.numInLine += 1
		self.myNumberInLine = person.numInLine
		print(myNumberInLine)

	

class bank:

	def __init__(self, line):
		if (line == None):
			self.line = []
		self.line = line

	def enqueue(self, person):
		self.line.append(person)

	def dequeue(self):
		self.line.pop(0)

	def printLine(self):
		for i in range (0, len(self.line)):
			print(self.line[i].myNumberInLine)

		

length = 10
people = [length]
for i in range(0, length):
	people.append(person())

line = [people[0], people[1], people[2]]


b = bank(line)
b.enqueue(person())




print(b.line)
b.printLine()