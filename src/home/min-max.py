def min(*args, **kwargs):
	return get_value_correct(args, kwargs, False)


def max(*args, **kwargs):
	return get_value_correct(args, kwargs, True)

def get_value_correct(values, kwargs, reverse=False):
	key = kwargs.get("key", None)
	for v in values:
		if type(v) == list:
			values = tuple(v) if len(values) == 1 else tuple(sorted(values, key=lambda values: values[0], reverse=reverse))
		elif type(v) == str:
			values = tuple(''.join(sorted(v)))
		elif type(v) == bool:
			pass
		elif type(v) not in (int, float, long, complex):
			values = tuple(v)
		break
	return sorted(values, key=key, reverse=reverse)[0]

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert max(3, 2) == 3, "Simple case max"
	assert min(3, 2) == 2, "Simple case min"
	assert max([1, 2, 0, 3, 4]) == 4, "From a list"
	assert min("hello") == "e", "From string"
	assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
	assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"

	# Tester checks
	assert max([0]) == 0, 'Extra #1'
	assert min((9,)) == 9, 'Extra #2'
	assert max(range(6)) == 5, 'Extra #3'
	assert min(abs(i) for i in range(-10, 10)) == 0, 'Extra #4'
	assert max(x + 5 for x in range(6)) == 10, 'Extra #5'
	assert max(filter(str.isalpha,"@v$e56r5CY{]")) == 'v', 'Extra #6'
	assert min({1, 2, 3, 4, -10}) == -10, 'Extra #7'
	assert max(set('djsaljldsklfjzx')) == 'z', 'Extra #8'
	assert min(set('djsaljldsklfjzx')) == 'a', 'Extra #9'
	assert max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]) == [7], 'Extra #10'
	assert min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum) == [1,2,3], 'Extra #11'
	assert max(True, False, -1, key=lambda x: not x) == False, 'Extra #12'
	assert min(True, False, -1) == -1, 'Extra #13'
	
