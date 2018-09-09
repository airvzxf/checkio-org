#!/usr/bin/python
import math

def checkio(data):
	bill_divisible = 5
	commission_percentage = 0.01
	commission_money = 0.5

	balance, withdrawals = data
	for withdraw in withdrawals:
		if withdraw < balance:
			if withdraw % bill_divisible == 0:
				percentage = withdraw * commission_percentage
				balance = int(math.floor(balance - withdraw - commission_money - percentage))
	return balance

if __name__ == '__main__':
	printcheckio([120, [10, 13, 20, 120, 30]])
	checkio([120, [200, 10]])
	checkio([120, [3, 10]])
	checkio([120, [200 , 119]])
	checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]])
