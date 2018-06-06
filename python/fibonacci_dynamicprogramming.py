import numpy as np
import math as m


myDict = {}

def getFib(fib):
	if (fib in myDict):
		return myDict[fib]
	else:
		if (fib <= 1):
			x = 1
			myDict[fib] = x
		else:
			x1 = getFib(fib-1)
			x2 = getFib(fib-2)
			myDict[fib-1] = x1
			myDict[fib-2] = x2
			x = x1 + x2
			myDict[fib] = x
		
		return x



# myDict = {}

# def getFib(fib):

# 	if(fib in myDict):
# 		return myDict[fib]
# 	else:
# 		if (fib <= 1):
# 			x = 1
# 			myDict[fib] = x
# 		else:
# 			x1 = getFib(fib-1)
# 			x2 = getFib(fib-2)
# 			x = x1 + x2
# 			myDict[fib] = x
			

# 		return x

num = 998

myFib = getFib(num)
count = 0
print(myFib)
print(myDict)
#print(count)
# 0 1 2 3 4 5 6  7
# 1 1 2 3 5 8 13 21

print(type(myDict[num]))