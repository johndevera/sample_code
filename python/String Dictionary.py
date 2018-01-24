# Given a string, print out all of the unique characters and the number of times it appeared in the string.

#sen = "eeisssanfifejs"

#x = {}
#for i in range(0, len(sen)):
#	if (x.get(sen[i]) != None): # if key exists
#		x[sen[i]] += 1
#	else: 
#		x[sen[i]] = 1
#print(x)



sen = "eeisssanfifejs"

x = {}

for i in range(0, len(sen)):
	if sen[i] in x:
		x[sen[i]] += 1
	else:
		x[sen[i]] = 1

print(x)



