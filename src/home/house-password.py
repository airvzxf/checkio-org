import re

def checkio(data):
	'Return True if password strong and False if not'
	if re.search(r'(?=^.{10,}$)(?=.*\d)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', data):
		return True
	return False

if __name__ == '__main__':
	assert checkio('A1213pokl')==False, 'First'
	assert checkio('bAse730onE4')==True, 'Second'
	assert checkio('asasasasasasasaas')==False, 'Third'
	assert checkio('QWERTYqwerty')==False, 'Fourth'
	assert checkio('123456123456')==False, 'Fifth'
	assert checkio('QwErTy911poqqqq')==True, 'Sixth'
	print 'All ok'