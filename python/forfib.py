


def fib(num):

	fib1 = 1
	fib2 = 1

	if num <= 1:
		return 1

	for i in range (1, num):
		fib = fib1 + fib2
		fib1 = fib2
		fib2 = fib
	return fib



print(fib(3))