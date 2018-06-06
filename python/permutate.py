
s = "xacxzaa"
b = "fxaazxacaaxzoecaxaxaxaz"

def findPermutation(s): #returns dictionary of permutations of s
	myDict = {}
	myDict = permutate(s,myDict)
	return myDict


def permutate(s, myDict):
	# I want to take s and hold the first element as pivot
	# Compare pivot with each element and swap and save each entry in the dictionary
	# Remove pivot from string and do recurssive call on S
	# if length is 2 we have reached the end. Swap last two elements, save to myDict and return myDict
	LHS_pivot = s[0]
	RHS = s[1:]
	if(len(RHS)>2):
		for i in range(len(RHS)):
			perm = swap(LHS_pivot, RHS, i)
			myDict[perm] = 1
			myDict = permutate(RHS, myDict) 
	else:
		swap(LHS_pivot, RHS, 0)

	return myDict

def swap(LHS, RHS, i):
	LHS = list(LHS)
	RHS = list(RHS)
	temp = LHS[0]
	LHS[0] = RHS[i]
	RHS[i] = temp
	return str(LHS + RHS)



myDict = findPermutation(s)
print("Number of occurances: ", len(myDict))
print(myDict)