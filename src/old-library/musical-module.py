def checkio(v):
	'Calculate the greatest common divisor of two numbers'
	a, b = v
	while b:
		a, b = b, a % b
	return a

if __name__ == '__main__':
	assert checkio((12, 8)) == 4, "First"
	assert checkio((14, 21)) == 7, "Second"
	assert checkio((13, 11)) == 1, "Third"
	print 'All ok'