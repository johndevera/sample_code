# Write a function that takes in a string and returns whether the string follows the "i before e except after c" rule.  

# Create a basic minesweeper game that allows for board creation with custom height, width and number of mines. Create a <click> function that will take in a board location and return whether the user has won, lost, or the number of surrounding mines.  

# Prove two words are palindromes

# Given a string, print out all of the unique characters and the number of times it appeared in the string.  

# How to enqueue and dequeue an array of people in a bank  

# Fizzbuzz

# sort a list then reverse it  


# Design
# Design a kitchen appliance with X constraint  
# Design a media center
# Phone: what data structures would you use to keep track of a group of people? How would you rate how good a product is? Pick a product that you really like using, tell us why, what is something you would change about it if you could (aka something you don't like) and how?
# How would you test sunglasses?  
# What is your favorite/least favorite Microsoft product and why? How would you change it to make it better?  
# Describe the internet to someone in elementary school  


ei = "receive"
ie = "lie"

def determineIE(word):
	for i in range(0, len(word)-1):
		if (word[i] == 'e' and word[i+1] == 'i'):
			return True
	return False

print(determineIE("ei"))








