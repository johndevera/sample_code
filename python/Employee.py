
class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last
		#self.email = first + '.' + last + '@email.com'

	@property
	def email(self):
		return ('{}.{}@email.com'.format(self.first, self.last))

	@property
	def fullName(self):
		return ('{} {}'.format(self.first, self.last))

	@fullName.setter
	def fullName(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@fullName.deleter
	def fullName(self):
		print("Delete Name!")
		self.first = None
		self.last = None

emp_1 = Employee("John", "Smith")

emp_1.fullName = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullName)

del emp_1.fullName
print(emp_1.email)


