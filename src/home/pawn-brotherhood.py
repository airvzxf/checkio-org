def safe_pawns(pawns):
	safe = 0
	int_a = ord('a')
	int_h = ord('h')

	for pawn in pawns:
		col_int = ord(pawn[0])
		row = int(pawn[1])

		pawn_left = chr(col_int-1)+str(row-1)
		pawn_right = chr(col_int+1)+str(row-1)
		if pawn_left in pawns or pawn_right in pawns:
			safe += 1

	return safe

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
	assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
