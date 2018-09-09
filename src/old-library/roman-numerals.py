roman = {
	0:'',
	1:'I',
	5:'V',
	10:'X',
	50:'L',
	100:'C',
	500:'D',
	1000:'M',
}
def checkio(n):
	'return roman numeral using the specified integer value from range 1...3999'
	s = str(n)
	d = len(s)
	r = ""
	# print "s: ",s
	for x in range(d):
		a = 0
		b = 0
		c = 0
		di = 10 ** (d-x-1)
		sn = int(s[x])
		if sn in range(1,4):
			b = 1*di
			c = sn
		if sn == 4:
			a = 1*di
			b = 5*di
			c = 1
		elif sn == 5:
			a = 5*di
		elif sn in range(6, 9):
			a = 5*di
			b = 1*di
			c = sn-5
		elif sn == 9:
			a = 1*di
			b = 10*di
			c = 1

		# print "x: ",x
		# print "s[x]: ",s[x]
		# print "sn: ",sn
		# print "di: ",di
		# print "n: ",n
		# print "a: ",a
		# print "b: ",b
		# print "c: ",c
		r = r + roman[a] + (roman[b] * c)
		# print "r: ",r
	print "*** n: ",n
	print "*** r: ",r
	print "---"
	return r

if __name__ == '__main__':
	for x in range(0, 1001, 1):
		checkio(x)
	# for x in range(5, 10):
	# 	checkio(x)
	# for x in range(0, 100, 10):
	# 	checkio(x)
	# checkio(9)
	# checkio(19)
	# checkio(69)
	# checkio(90)
	# assert checkio(6) == 'VI', 'First'
	# assert checkio(76) == 'LXXVI', 'Second'
	# assert checkio(499) == 'CDXCIX', 'Third'
	# assert checkio(3888) == 'MMMDCCCLXXXVIII', 'Fourth'
	print 'All ok'