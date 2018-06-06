
x = "Hello, my name is john, what is your, name?"
puncDict = {',': 1, '"': 1, '?': 1, '&': 1, }
for j in range(len(puncDict)):
	delimeter = next(iter(puncDict))
	print(delimeter)
	# delimeter = puncDict[j]	
	myList = x.split(delimeter)
	temp_string = ""
	for i in range(len(myList)):
		temp_string = temp_string + myList[i]
		#print (temp_string)

print (temp_string)

a = [1,2]
print (a)
b = "hi"
c = "g"
listB = list(b)
print(b)
print(listB)
print(listB.strip(","))
print(str(listB.strip(',')))
print(len(puncDict))
# puncDict = {',': 1, '"': 1, '?': 1, '&': 1, }
# for i in range(len(x)):
# 	if x[i] in 

# myDict = {}
# for i in range(len(myList)):
# 	if myList[i] in myDict:
# 		myDict[myList[i]] += 1
# 		# print(i, myDict[myList[i]])
# 	else:
# 		myDict[myList[i]] = 1


# print(myDict)
