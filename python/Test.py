

#class oo in python

class Employee:
	
	num_of_emps =0
	raise_amount = 1.04;

	def __init__(self, first, last, pay): #like constructor
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last +'@company.com'

		Employee.num_of_emps += 1


	def fullName(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		#self.raise_amount = raise_amount
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod #alternative constructor
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

class Developer(Employee):

	def __init__(self, first, last, pay, prog_lang):
		super(Developer, self).__init__(first, last, pay)
		self.prog_lang = prog_lang	
	
class Manager(Employee):
	pass

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

 

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))