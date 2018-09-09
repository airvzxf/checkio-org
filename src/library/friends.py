class Friends:
	def __init__(self, connections):
		self.connections = tuple(connections)

	def add(self, connection):
		for c in self.connections:
			if c <= connection:
				return False
		self.connections += tuple([connection])
		return True

	def remove(self, connection):
		total = len(self.connections)
		self.connections = tuple(x for x in self.connections if not x <= connection)
		return True if len(self.connections) < total else False

	def names(self):
		names = set()
		for c in self.connections:
			for v in c:
				if v not in names:
					names.add(v)
		return names

	def connected(self, name):
		connected = set()
		for c in self.connections:
			if name in c:
				connected |= set(x for x in c if x != name)
		return connected


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
	digit_friends = Friends([{"1", "2"}, {"3", "1"}])
	assert letter_friends.add({"c", "d"}) is True, "Add"
	assert letter_friends.add({"c", "d"}) is False, "Add again"
	assert letter_friends.remove({"c", "d"}) is True, "Remove"
	assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
	assert letter_friends.names() == {"a", "b", "c"}, "Names"
	assert letter_friends.connected("d") == set(), "Non connected name"
	assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
