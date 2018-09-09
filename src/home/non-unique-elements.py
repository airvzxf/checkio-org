#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
	#Your code here+
	#It's main function. Don't remove this function
	#It's used for auto-testing and must return a result for check.

	#replace this for solution
	list_index = 1
	list_new = []
	for d in data:
		if d in list_new:
			list_new.append(d)
		for c in data[list_index:]:
			if d in list_new:
				break
			if d == c:
				list_new.append(d)
				break
		list_index += 1
	return list_new

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert isinstance(checkio([1]), list), "The result must be a list"
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

	#~ checkio([1, 2, 3, 1, 3])
	#~ checkio([1, 2, 3, 4, 5])
	#~ checkio([5, 5, 5, 5, 5])
	#~ checkio([10, 9, 10, 10, 9, 8])
