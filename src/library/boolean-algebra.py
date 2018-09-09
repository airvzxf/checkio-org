OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):

	result = False

	if operation == 'conjunction':
		result = x and y
	elif operation == 'disjunction':
		result = x or y
	elif operation == 'implication':
		result = (not x) or y
	elif operation == 'exclusive':
		result = 0 if x == y else 1
	elif operation == 'equivalence':
		result = 1 if x == y else 0

	print '%s | %d %d = %d' % (operation, x, y, result)
	return result

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert boolean(1, 0, u"conjunction") == 0, "and"
	assert boolean(1, 0, u"disjunction") == 1, "or"
	assert boolean(1, 1, u"implication") == 1, "material"
	assert boolean(0, 1, u"exclusive") == 1, "xor"
	assert boolean(0, 1, u"equivalence") == 0, "same?"

	print ''
	assert boolean(0, 0, u'conjunction') == 0, '0 0 | conjunction'
	assert boolean(1, 0, u'conjunction') == 0, '1 0 | conjunction'
	assert boolean(0, 1, u'conjunction') == 0, '0 1 | conjunction'
	assert boolean(1, 1, u'conjunction') == 1, '1 1 | conjunction'
	print ''
	assert boolean(0, 0, u'disjunction') == 0, '0 0 | conjunction'
	assert boolean(1, 0, u'disjunction') == 1, '1 0 | conjunction'
	assert boolean(0, 1, u'disjunction') == 1, '0 1 | conjunction'
	assert boolean(1, 1, u'disjunction') == 1, '1 1 | conjunction'
	print ''
	assert boolean(0, 0, u'implication') == 1, '0 0 | implication'
	assert boolean(1, 0, u'implication') == 0, '1 0 | implication'
	assert boolean(0, 1, u'implication') == 1, '0 1 | implication'
	assert boolean(1, 1, u'implication') == 1, '1 1 | implication'
	print ''
	assert boolean(0, 0, u'exclusive') == 0, '0 0 | exclusive'
	assert boolean(1, 0, u'exclusive') == 1, '1 0 | exclusive'
	assert boolean(0, 1, u'exclusive') == 1, '0 1 | exclusive'
	assert boolean(1, 1, u'exclusive') == 0, '1 1 | exclusive'
	print ''
	assert boolean(0, 0, u'equivalence') == 1, '0 0 | equivalence'
	assert boolean(1, 0, u'equivalence') == 0, '1 0 | equivalence'
	assert boolean(0, 1, u'equivalence') == 0, '0 1 | equivalence'
	assert boolean(1, 1, u'equivalence') == 1, '1 1 | equivalence'
	print ''
