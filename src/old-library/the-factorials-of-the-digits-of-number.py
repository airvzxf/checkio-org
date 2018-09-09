import math

def checkio(d):
	'calculate sum of the factorials for all digits of the specified positive integer number.'
	s = str(d)
	t = 0
	for x in s:
		t = t + math.factorial(int(x))
	return t

if __name__ == '__main__':
	assert checkio(100) == 3, 'First'
	assert checkio(222) == 6, 'Second'
	assert checkio(1234) == 33, 'Third'
	print 'All ok'