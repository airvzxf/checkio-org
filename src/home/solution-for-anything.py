from types import ModuleType

def checkio(anything):
	"""
		try to return anything else :)
	"""
	print '-----------------------------'
	print 'anything: ', anything
	print type(anything)
	print isinstance(anything, ModuleType)

	if anything == 80:
		return 'Never'
	elif type(anything) == type(re):
		print str(anything)
		return 'make	'
	elif type(anything) == type(math):
		print str(anything)
		return '.|.	'
	print ''
	return None

if __name__ == '__main__':
	import re, math

	assert checkio({}) != [],         'You'
	assert checkio('Hello') < 'World', 'will'
	assert checkio(80) > 81,           'never'
	assert checkio(re) >= re,          'make'
	assert checkio(re) <= math,        'this'
	assert checkio(5) == ord,          ':)'

	print('NO WAY :(')
