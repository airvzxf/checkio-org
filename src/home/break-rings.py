def break_rings(rings):
	print rings
	rings = [list(r) for r in rings]
	rings.sort()

	rings_broken = 0
	uniques_rings = {}
	uniques_connections = {}

	for ring in rings:
		r, c = ring
		uniques_rings[r] = 0
		uniques_connections[c] = 0

	for ring in rings:
		r, c = ring
		if c in uniques_rings.keys(): uniques_rings[c] += 1
		uniques_connections[c] += 1

	while sum(uniques_rings.values()) > 0:
		for ring in rings:
			r, c = ring
			if uniques_rings[r] > 0:
				rings.remove(ring)
				rings_broken += 1
				uniques_rings[r] -= 1
				uniques_connections[c] -= 1
				if c in uniques_rings.keys(): uniques_rings[c] -= 1

		for ring in rings:
			r, c = ring
			if uniques_connections[c] > 1:
				rings.remove(ring)
				rings_broken += 1
				uniques_rings[r] -= 1
				uniques_connections[c] -= 1
				if c in uniques_rings.keys(): uniques_rings[c] -= 1

	print '---------------------------'
	print 'rings_broken: ', rings_broken
	print '---------------------------'
	print ''
	return rings_broken


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
	assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
	assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
	assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
