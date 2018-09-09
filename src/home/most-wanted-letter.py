import re
import collections

def checkio(text):

	letters = {}
	only_letters = re.compile(r'[^a-zA-Z]')
	text = re.sub(only_letters, '', text).lower()
	text = ''.join(sorted(text))

	for l in text:
		if letters.has_key(l.lower()):
			letters[l.lower()] = int(letters[l.lower()]) + 1
		else:
			letters[l.lower()] = 1
		pass

	letters = collections.OrderedDict(sorted(letters.items()))
	letters = list(sorted(letters, key=letters.__getitem__, reverse=True))

	#replace this for solution
	return letters[0]

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(u"Hello World!") == "l", "Hello test"
	assert checkio(u"How do you do?") == "o", "O is most wanted"
	assert checkio(u"One") == "e", "All letter only once."
	assert checkio(u"Oops!") == "o", "Don't forget about lower case."
	assert checkio(u"AAaooo!!!!") == "a", "Only letters."
	assert checkio(u"abe") == "a", "The First."
	print("Start the long test")
	assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
	print("The local tests are done.")
