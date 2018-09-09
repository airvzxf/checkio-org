def check_pangram(text):

	text = text.lower()

	for alphabetic in range(ord('a'), ord('z') + 1):
		if not chr(alphabetic) in text:
			return False
	
	return True

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
	assert not check_pangram("ABCDEF"), "ABC"
	assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
