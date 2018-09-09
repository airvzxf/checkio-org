def checkio(number):

	binary = len(str(bin(number)).replace('b', '').replace('0', ''))

	return binary

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(4) == 1
	assert checkio(15) == 4
	assert checkio(1) == 1
	assert checkio(1022) == 9
