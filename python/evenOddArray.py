#given an array, find all the even numbers, and list them first, followed by the odd numbers

#My solution: Use two for loops with two indexs.
#First index "i" is to look for Even via N%2=0. This stops when found N%2=1
#Second index "j" starts at i+1 and starts counting forward unitl N%2=0, which means an even found. 
#Swap the two numbers, since number order doesn't matter, just position of even and odds

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)

# length = len(numbers)
# for i in range(0, length):
# 	if(numbers[i]%2 !=0): #if found odd
# 		for j in range(i+1, length):
# 			if(numbers[j]%2 == 0): #if found even, SWAP numbers[i] and numbers[j]
# 				temp = numbers[i]
# 				numbers[i] = numbers[j]
# 				numbers[j] = temp
# 				break

# print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

length = len(numbers)
for i in range(0, length):
	if(numbers[i]%2 !=0): #if found odd
		for j in range(i+1, length):
			count = 0
			if(numbers[j]%2 == 0): #if found even, SWAP numbers[i] and numbers[j]
				count += 1
				
				temp = numbers[i]
				numbers[i] = numbers[j]
				numbers[j] = temp
				break

print(numbers)


