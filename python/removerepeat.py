def removerepeat(s):
	x = {}
	for i in range(0, len(s)):
		print(s[i])
		l = []
		if s[i] in x:
			x[s[i]].append(i)
		else:
			l.append(i)
			x[s[i]] = l
		print(x[s[i]])
	#length = len(x[s[i]])
	for i in range(0, len(s)):
		length = len(x[s[i]])
		if length > 1:
			for j in range (0, length):
				s = s.replace(str(x[s[i]][j]), "")
	return s

s = "mam"
	

new_s = removerepeat(s)
print(new_s)
print(len(new_s))