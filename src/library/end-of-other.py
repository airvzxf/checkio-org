def checkio(words_set):

	if len(words_set) < 2:
		return False

	# Convert set to list
	words_list = []
	for key in words_set:
		words_list.append(key)

	# Sort list by max lenght to min lenght
	words_list.sort(key = len, reverse=True)


	#Search last letters in big word
	found = False
	word = ''
	for first in range(len(words_list)):
		for second in range(first + 1, len(words_list)):
			second_len = len(words_list[second])
			if words_list[first][-second_len:] == words_list[second]:
				found = True
				word = words_list[first][:-second_len] + words_list[second].upper()
				break
	
	return found

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
	assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
	assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
	assert checkio({u"one"}) == False, "Only One"
	assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"
