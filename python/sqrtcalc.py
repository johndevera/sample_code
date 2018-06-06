import numpy as np
# y = x*x
# x = y/x

def test(x, y):
	if (close_enough(x/y, y)):
		return y
	else:
		return test(x, betterguess(x, y))


def close_enough(a, b):
	return (np.abs(a - b) < 0.001)

def betterguess(x, y):
	return ((y + x/y) / 2 )


print(test(16, 1))