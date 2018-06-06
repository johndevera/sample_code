num = 1000
num1 = 3
num2 = 5

def addword(i, word, num, out):
	if (i % num == 0): out = out + word
	return out

for i in range(1, num):
	output = ""

	output = addword(i, "fizz", 3, output)
	output = addword(i, "buzz", 5, output)
	output = addword(i, "john", 7, output)

	# if (i % num1 == 0): output = output + "Fizz"
	# if (i % num2 == 0): output = output + "Buzz"

	if (len(output) == 0): output = i
	print(output)