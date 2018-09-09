def check_connection(network, first, second):

	network_list = []

	for n in network:
		network_list.append(n)

	(my_friend, knows) = friends_near(network_list, first, second)

	return my_friend


def friends_near(friends, friend_1, friend_2, tab = 0):

	friends_total = len(friends)
	knows = ''
	my_friend = False
	r = 0

	if 	friends_total == 0 or friend_1 == friend_2:
		return my_friend, knows


	#~ print (" "*tab) + 'Count friends: ', friends_total
	#~ print (" "*tab) + 'friends: ', friends
	#~ print (" "*tab) + 'friend_1: ', friend_1
	#~ print (" "*tab) + 'friend_2: ', friend_2
	#~ print (" "*tab) + 'tab: ', tab
	#~ print ''

	for relationship in friends:
		k1, hyper, k2 = relationship.partition('-')

		if friend_1 == k1 or friend_1 == k2:
			know_found = None
			del friends[r]

			if friend_1 == k1:
				know_found = k2
			else:
				know_found = k1

			if k1 == friend_2 or k2 == friend_2:
				knows = {friend_1: know_found}
				return True, knows


			tab += 1
			my_friend, k = friends_near(friends, know_found, friend_2, tab)
			tab -= 1

			knows = { friend_1 : k }

		r += 1

	return my_friend, knows


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"scout2", "scout3") == True, "Scout Brotherhood"
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"super", "scout2") == True, "Super Scout"
	assert check_connection(
		("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
		 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
		"dr101", "sscout") == False, "I don't know any scouts."
