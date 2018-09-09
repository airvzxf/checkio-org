def count_words(text, words):

	words_count = 0
	text = text.lower()

	for word in words:
		if word in text:
			words_count += 1

	return words_count


if __name__ == '__main__':
	#These uu"1sserts" using only for self-checking and not necessary for auto-testing
	assert count_words(u"How aresjfhdskfhskd you?", {u"how", u"are", u"you", u"hello"}) == 3, "Example"
	assert count_words(u"Bananas, give me bananas!!!", {u"banana", u"bananas"}) == 2, "BANANAS!"
	assert count_words(u"Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
					   {u"sum", u"hamlet", u"infinity", u"anything"}) == 1, "Weird text"
