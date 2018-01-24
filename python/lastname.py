
class ParentClass:
	
	lastName = "de Vera"

	def __init__(self, strName):
		self.strName = strName

	def printName(self):
		print(self.strName)

	def printLastName(self):
		print(self.lastName)



class ChildClass(ParentClass):
	def __init__(self, strName, childNum):
		super().__init__(strName)
		self.childNum = childNum

	def changeLastName(self, newLastName):
		self.lastName = newLastName

	def printChildNum(self):
		print("I am child number " + str(self.childNum))


parent = ParentClass("Dad")
parent.printName()
parent.printLastName()

child = ChildClass("John", 1)
child.printName()
child.printChildNum()

ChildClass.printLastName(child)
ChildClass.changeLastName(child, "XXX")
#child.changeLastName("dv")
child.printLastName()
parent.printLastName()



