#prove string is palindrome
#even or odd length does not affect resutl


def isPalindrome(sen):
	
	length = int(len(sen) / 2)

	j = len(sen) - 1
	for i in range(0, length):
		if(sen[i] == sen[j]):
			j -= 1
		else:
			return False
	return True

sen = "asbbsa"

print(isPalindrome(sen))









