sen = "hello, my name is john!"

length = len(sen)

begin = 0
end = 0
for i in range(0, length):
	#print(i)

	if sen[i] == "," or sen[i] == "!":
		#print(sen[i], "sen i")
		end = i
		temp = sen[begin:end]
		temp_range = end - begin
		#print(temp_range, "temp_range")
		for j in range(1, temp_range+1):
			print(temp[-j])
		print(sen[i])
		begin = i+1




	