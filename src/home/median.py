def checkio(data):
	data.sort()
	data_total = len(data)
	data_split = int((data_total / 2) + 0.5)
	data_median = None


	if data_total % 2:
		data_median = data[data_split]
	else:
		data_median = ( float(data[data_split-1]) / 2 ) + ( float(data[data_split]) / 2 )

	return data_median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
	assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
	assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
	assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
	print("Start the long test")
	assert checkio(range(1000000)) == 499999.5, "Long."
	print("The local tests are done.")
