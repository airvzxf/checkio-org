def checkio(arr, lvl=0):
	'convert all elements in arr in one row'
	ar = list()
	for x in arr:
		if  type(x) == list:
			x = checkio(x, 1)
		if type(x) == list:
			ar = ar + x
		else:
			ar.append(x)
	return ar

if __name__ == '__main__':
	assert checkio([1,2,3]) == [1,2,3], 'First'
	assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
	assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]]) == [2,4,5,6,6,6,6,6,7], 'Third'
	print 'All ok'
