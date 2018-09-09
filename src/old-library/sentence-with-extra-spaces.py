import re

def checkio(string):
	'return sentence without extra spaces'
	pattern = re.compile(r'\s+')
	sentence = re.sub(pattern, ' ', string)
	return sentence

if __name__ == '__main__':
	assert checkio('I  like   python') == "I like python", 'First'
	print 'All ok'
