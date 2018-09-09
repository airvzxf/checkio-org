def count_gold(rows):
	last_row = [[0]]

	# Get each row
	for row in rows:
		route = []
		column = 0

		# Get each column with amount
		for amount in row:

			# If it's first value only sum with before row and first column
			if column == 0:
				route.append([int(amount)+int(last_row[0][0])])
			# If it's first value only sum with before row and last column
			elif column == len(row)-1:
				route.append([int(amount)+int(last_row[-1][0])])
			# Generate values intermediate
			else:
				last = []
				# Get in a before row: 1 before column and 1 next column
				for a in last_row[column-1:column+1]:
					for b in a:
						last.append(int(amount)+int(b))
				# Save in route
				route.append(last)

			column += 1

		# Save the new last_row list
		last_row = list(route)

	# Convert sublists in a one list, then order A-Z, then get the last value
	return int(sorted(sum(route, []))[-1])

if __name__ == '__main__':
	assert count_gold((
		(1,),
		(2, 3),
		(3, 3, 1),
		(3, 1, 5, 4),
		(3, 1, 3, 1, 3),
		(2, 2, 2, 2, 2, 2),
		(5, 6, 4, 5, 6, 4, 3)
	)) == 23, '#1'
	assert count_gold((
		(1,),
		(2, 1),
		(1, 2, 1),
		(1, 2, 1, 1),
		(1, 2, 1, 1, 1),
		(1, 2, 1, 1, 1, 1),
		(1, 2, 1, 1, 1, 1, 9)
	)) == 15, '#2'
	assert count_gold((
		(9,),
		(2, 2),
		(3, 3, 3),
		(4, 4, 4, 4)
	)) == 18, '#3'
