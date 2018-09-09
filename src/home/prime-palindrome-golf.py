def golf(n):
	while n:
		n+=1
		for x in range(2,n):
			if n%x==0:break
		else:
			l=len(str(n))
			if str(n)[:l/2]==str(n)[::-1][:l/2]:return n

if __name__ == '__main__':
	assert golf(2) == 3, 'Test #1'
	assert golf(13) == 101, 'Test #2'
	assert golf(101) == 131, 'Test #3'
	#~ assert golf(10000) == 10301, 'Test #4'
	#~ assert golf(98389) == 98689, 'Test #5'
