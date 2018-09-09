#!/usr/bin/python
def checkio(offers):
	'''
		the amount of money that Petr will pay for the ride
	'''
	initial_sofi, raise_sofi, initial_oldman, reduction_oldman = offers
	offer = 0

	while (initial_sofi <= initial_oldman):

		initial_sofi = initial_sofi + raise_sofi

		if initial_sofi < initial_oldman:
			offer = initial_sofi
		else:
			offer = initial_oldman

		initial_oldman = initial_oldman - reduction_oldman

	return offer



if __name__ == '__main__':
	#checkio([150, 50, 1000, 100])
	#checkio([150, 50, 900, 100])
	#checkio([500, 300, 700, 100])
	#checkio([500, 300, 700, 50])
	#checkio([150, 50, 330, 100])
	checkio([200, 100, 200, 100])
	#assert checkio([150, 50, 1000, 100]) == 450, 'First'
	#assert checkio([150, 50, 900, 100]) == 400, 'Second'
	print 'All is ok'
