
x = [5, 2, 3, 10, 22, 40, 1, 4]
x = [22, 20]

first = None
second = None

first = x[0]
for i in range(1,len(x)):

	if (x[i] > first):
		second = first
		first = x[i]
	print(i, first, second)

print(second)
