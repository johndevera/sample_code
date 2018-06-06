leftFlag = False
rightFlag = False

lp = x[0] // first position of list
rp = x[-1] // last position of list
center = x[len(x)/2] // center position of list

notDone = True

while(notDone):
	index = 1
	for i in range(index:len(x)):
		if (leftFlag && rightFlag):
			index = i
			break

		if lp > center: // traverse from LHS
			leftFlag = True

		if rp < center: //traverse from RHS
			rightFlag = True


	swap(lp, rp, x, index)

	if (x.reachedEnd()):
		break


def swap(lp, rp, x):
	temp = lp
	lp = rp
	rp = temp

	x[i] = lp
	x[-(i+1)] = rp


