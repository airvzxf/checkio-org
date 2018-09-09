def checkio(game_result):
	# Vars
	win = {'X':{}, 'O':{}}
	winner = 'D'

	# Create value matix, separete to Rows, Cols and Diagonals
	for a in range(3):
		win['X'].update({'row'+str(a):0, 'col'+str(a):0, 'dig0':0, 'dig1':0})
		win['O'].update({'row'+str(a):0, 'col'+str(a):0, 'dig0':0, 'dig1':0})

		# Create Rows and Cols Matrix
		for b in range(3):
			letter_row = str(game_result[a][b])
			letter_col = str(game_result[b][a])
			letter_dig0 = str(game_result[b][b])
			letter_dig1 = str(game_result[b][2-b])

			# Create Row
			if letter_row != '.':
				win[letter_row]['row'+str(a)] += 1

			# Create Col
			if letter_col != '.':
				win[letter_col]['col'+str(a)] += 1

			# Create Diagonals
			if a == 2:
				
				# Create Diagonal 0
				if letter_dig0 != '.':
					win[letter_dig0]['dig0'] += 1
				
				# Create Diagonal 1
				if letter_dig1 != '.':
					win[letter_dig1]['dig1'] += 1

	# Search the first gamer with 3 ponints, if it isn't winner was declaret with D
	for letter_key, letter_value in win.iteritems():
		for line_key, line_value in letter_value.iteritems():
			if line_value == 3:
				winner = letter_key
			
	return winner

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio([
		u"X.O",
		u"XX.",
		u"XOO"]) == "X", "Xs wins"
	assert checkio([
		u"OO.",
		u"XOX",
		u"XOX"]) == "O", "Os wins"
	assert checkio([
		u"OOX",
		u"XXO",
		u"OXX"]) == "D", "Draw"
	assert checkio([
		u"O.X",
		u"XX.",
		u"XOO"]) == "X", "Xs wins again"

