FIRST_TEN = ["zero ", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine "] 
SECOND_TEN = ["ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
OTHER_TENS = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
HUNDRED = "hundred "


def checkio(number):
	number_str = str(number)
	total_dig = len(number_str)
	number_letter = ""

	if number > 999:
		return False
	if number == 0:
		number_letter = FIRST_TEN[0]
	if number > 99:
		number_letter = FIRST_TEN[int(number_str[total_dig-3])] + HUNDRED
		number = number - int(number_str[total_dig-3]+'00')
	if number > 19:
		if number % 10 == 0:
			number_letter = number_letter + OTHER_TENS[int(number_str[total_dig-2])]
			number = number - int(number_str[total_dig-2]+number_str[total_dig-1])
		else:
			number_letter = number_letter + OTHER_TENS[int(number_str[total_dig-2])]
			number = number - int(number_str[total_dig-2]+'0')
	if number > 9:
		number_letter = number_letter + SECOND_TEN[int(number_str[total_dig-1])]
		number = number - int(number_str[total_dig-2]+number_str[total_dig-1])
	if number > 0:
		number_letter = number_letter + FIRST_TEN[int(number_str[total_dig-1])]
		number = number - int(number_str[total_dig-1])
	return number_letter.strip()


if __name__ == '__main__':
	checkio(133)
	checkio(212)
	checkio(905)
	checkio(752)
	checkio(979)
	checkio(530)
	checkio(30)
	checkio(53)
	checkio(78)
	checkio(10)
	checkio(12)
	checkio(15)
	checkio(19)
	checkio(20)
	checkio(5)
	checkio(7)
	checkio(0)
	# assert checkio(4) == 'four', "First"
	# assert checkio(133) == 'one hundred thirty three', "Second"
	# assert checkio(12)=='twelve', "Third"
	# assert checkio(101)=='one hundred one', "Fifth"
	# assert checkio(212)=='two hundred twelve', "Sixth"
	# assert checkio(40)=='forty', "Seventh, forty - it is correct"

	print 'All ok'