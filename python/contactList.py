import numpy as np

class letter:

	def __init__(self, character):
		pass

class ContactList:

	count = 0

	def __init__(self):
		self.ledger = {}
		pass


	def addContact(self, name, number):
		if name in self.ledger:
			if self.ledger[name] == number:
				print("You cannot add a duplicate name.", self.ledger[name])
			else:
				ContactList.count = ContactList.count + 1
				self.ledger[name + str(ContactList.count)] = number
				ContactList.count += 1
				print("New contact added")

		else:
			self.ledger[name] = number
			ContactList.count += 1
			print("New contact added")


		# if (self.ledger.has_key(name)):
		# 	print("not able to add duplicate")
		# else:
		# 	self.ledger[name] = number
		# 	count = ContactList.count + 1
		# 	print("successfully added contact")

		# self.contactCount = contactList.count + 1 #this is to assign the value of the contact
		# contactList.count = countactList.count + 1 # this is to update the total class number
		

myList = ContactList()

myList.addContact("John", 6047803484)
print(myList.ledger)
myList.addContact("John", 26)
print(myList.ledger)
myList.addContact("Laura", 913)
print(myList.ledger)
myList.addContact("John", 26)
print(myList.ledger)
myList.addContact("Laura", 913)
print(myList.ledger)




# 	def __init__(self, letter):

# 		self.character = letter
# 		self.numChildWords = 0
# 		self.next = None
# 		self.myDictionary = {	"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,  
# 								"g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, 
# 								"m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,  
# 								"s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
# 								"y": 0, "z": 0	}

# 		self.splitWord = None
# 	def addChild(self, node):
# 		self.next = node

# 	def addWord(self, word):
# 		length = len(word)
# 		self.splitWord = list(word)
		
# 		for i in range(0:length):
# 			self.next = new node(splitWord[i])



# one = node("a")
# two = node("b")
# one.addWord("that")
# print (one.splitWord)
