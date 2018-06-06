
num = 8

#clear
mask = 1
mask = mask << 3
mask = ~mask
print("Clear: ", mask&num)


#set 4 + 8
mask = 1
mask = mask << 2
print("Set", mask|num)

