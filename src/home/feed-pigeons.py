def checkio(portions):

	if portions == 0:
		return 0

	minutes = 1
	birds_per_minute_last = 1

	while True:
		for minute in range(minutes):
			birds = 0
			birds_per_minute = get_birds_per_minute(minutes)

			for b in range(birds_per_minute):
				portions -= 1
				birds += 1

				if portions == 0:
					if birds_per_minute_last > birds:
						birds = birds_per_minute_last
					return birds

			minutes += 1
			birds_per_minute_last = birds_per_minute

	return 0



def get_birds_per_minute(minutes):
	minutes_total = 0
	for m in range(minutes + 1):
		minutes_total += m

	return minutes_total




if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(1) == 1, "1st example"
	assert checkio(2) == 1, "2nd example"
	assert checkio(5) == 3, "3rd example"
	assert checkio(10) == 6, "4th example"

	# Israel Roldan tests
	times_start = 0
	times = 20

	# Start test
	portions = 0
	birds = 0
	birds_per_minute_last = 0

	for minute in range(times_start, times + 1):

		if minute == 0:
			portions += 1

		birds_per_minute =  get_birds_per_minute(minute)

		for b in range(birds_per_minute):

			if b >= birds_per_minute_last:
				birds += 1

			print "Minute: %d  |  Portion: %d  |  Birds: %d" % (minute, portions, birds)
			assert checkio(portions) == birds, "Portion: %d, Birds: %d" % (portions, birds)
			portions += 1

		birds_per_minute_last = birds_per_minute

	#~ assert checkio(0) == 0, "Israel Roldan Test"
	#~ # 1st Minute
	#~ assert checkio(1) == 1, "Israel Roldan Test"
	#~ # 2nd Minute
	#~ assert checkio(2) == 1, "Israel Roldan Test"
	#~ assert checkio(3) == 2, "Israel Roldan Test"
	#~ assert checkio(4) == 3, "Israel Roldan Test"
	#~ # 3th Minute
	#~ assert checkio(5) == 3, "Israel Roldan Test"
	#~ assert checkio(6) == 3, "Israel Roldan Test"
	#~ assert checkio(7) == 3, "Israel Roldan Test"
	#~ assert checkio(8) == 4, "Israel Roldan Test"
	#~ assert checkio(9) == 5, "Israel Roldan Test"
	#~ assert checkio(10) == 6, "Israel Roldan Test"
	#~ # 4th Minute
	#~ assert checkio(11) == 6, "Israel Roldan Test"
	#~ assert checkio(12) == 6, "Israel Roldan Test"
	#~ assert checkio(13) == 6, "Israel Roldan Test"
	#~ assert checkio(14) == 6, "Israel Roldan Test"
	#~ assert checkio(15) == 6, "Israel Roldan Test"
	#~ assert checkio(16) == 6, "Israel Roldan Test"
	#~ assert checkio(17) == 7, "Israel Roldan Test"
	#~ assert checkio(18) == 8, "Israel Roldan Test"
	#~ assert checkio(19) == 9, "Israel Roldan Test"
	#~ assert checkio(20) == 10, "Israel Roldan Test"
	#~ # 5th Minute
	#~ assert checkio(21) == 10, "Israel Roldan Test"
	#~ assert checkio(22) == 10, "Israel Roldan Test"
	#~ assert checkio(23) == 10, "Israel Roldan Test"
	#~ assert checkio(24) == 10, "Israel Roldan Test"
	#~ assert checkio(25) == 10, "Israel Roldan Test"
	#~ assert checkio(26) == 10, "Israel Roldan Test"
	#~ assert checkio(27) == 10, "Israel Roldan Test"
	#~ assert checkio(28) == 10, "Israel Roldan Test"
	#~ assert checkio(29) == 10, "Israel Roldan Test"
	#~ assert checkio(30) == 10, "Israel Roldan Test"
	#~ assert checkio(31) == 11, "Israel Roldan Test"
	#~ assert checkio(32) == 12, "Israel Roldan Test"
	#~ assert checkio(33) == 13, "Israel Roldan Test"
	#~ assert checkio(34) == 14, "Israel Roldan Test"
	#~ assert checkio(35) == 15, "Israel Roldan Test"
