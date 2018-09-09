def checkio():
	return 13  # if you are Sheldon, I say this number is mistic

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert isinstance(checkio(), (int, float, complex))
