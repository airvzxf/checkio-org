from datetime import datetime

def days_diff(date1, date2):
	"""
		Find absolute diff in days between dates
	"""

	date1_str = '%s-%s-%s' % (str(date1[0]).zfill(4), str(date1[1]).zfill(2), str(date1[2]).zfill(2))
	date2_str = '%s-%s-%s' % (str(date2[0]).zfill(4), str(date2[1]).zfill(2), str(date2[2]).zfill(2))

	d1 = datetime.strptime(date1_str, "%Y-%m-%d")
	d2 = datetime.strptime(date2_str, "%Y-%m-%d")

	days = abs((d2 - d1).days)

	return days

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	days_diff((1,1,1), (9999,12,31))
	assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
	assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
	assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

