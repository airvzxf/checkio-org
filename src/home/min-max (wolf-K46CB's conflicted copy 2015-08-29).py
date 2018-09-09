import types

def min(*args, **kwargs):
	print 'MIN'
	print 'args: ', args
	print 'kwargs: ', kwargs
	#~ print 'type(args): ', type(args)
	#~ print 'type(kwargs): ', type(kwargs)
	#~ value = get_value_correct(args, kwargs, False)
	print '--------------------------------'
	print ''
	return get_value_correct(args, kwargs, False)


def max(*args, **kwargs):
	print 'MAX'
	print 'args: ', args
	print 'kwargs: ', kwargs
	#~ print 'type(args): ', type(args)
	#~ print 'type(kwargs): ', type(kwargs)
	#~ value = get_value_correct(args, kwargs, True)
	print '--------------------------------'
	print ''
	return get_value_correct(args, kwargs, True)

def get_value_correct(values, kwargs, reverse=False):
	key = kwargs.get("key", None)
	print ''
	print '--------'
	print 'values: ', values
	print 'type(values): ', type(values)
	print 'key: ', key
	print 'type(key): ', type(key)
	print ''

	for v in values:
		print 'v: ', v
		print 'type(v): ', type(v)
		if type(v) in (list, tuple):
			#~ print 'Fuck you list'
			values = tuple(v)
		elif type(v) == str:
			#~ print 'Fuck you Str'
			values = tuple(''.join(sorted(v)))
		elif type(v) == types.GeneratorType:
			print '*** Fuck you generator! Ohhh!'
			print 'v: ', tuple(v)
			values = sorted(v)
		break
	print ''
	#~ print '- values: ', values
	#~ value = sorted(values, key=key, reverse=reverse)[0]
	#~ print '+ values: ', values
	#~ print 'type(values): ', type(values)
	print 'value: ', sorted(values, key=key, reverse=reverse)[0]
	print '--------'
	print ''
	return sorted(values, key=key, reverse=reverse)[0]

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	#~ max(3, 2)
	#~ min(3, 2)
	#~ max([1, 2, 0, 3, 4])
	#~ min("hello")
	#~ max(2.2, 5.6, 5.9, key=int)
	#~ min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])

	#~ assert min((9,)) == 9, "CheckIO"
	min(abs(i) for i in range(-10, 10))
	#~ assert max(3, 2) == 3, "Simple case max"
	#~ assert min(3, 2) == 2, "Simple case min"
	#~ assert max([1, 2, 0, 3, 4]) == 4, "From a list"
	#~ assert min("hello") == "e", "From string"
	#~ assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
	#~ assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
