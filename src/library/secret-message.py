def find_message(text):
	"""Find a secret message"""

	secret = ''

	for word in text:
		if word[0].istitle(): secret += word[0]

	return secret

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert find_message(u"How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
	assert find_message(u"hello world!") == "", "Nothing"
	assert find_message(u"HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
