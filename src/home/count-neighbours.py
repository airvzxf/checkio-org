def count_neighbours(grid, row, col):
    grid_lenght = len(grid)
    neighbours = 0

    for a in range(-1, 2):
        if row+a >= 0 and row+a < len(grid):
            if col-1 >=0:
                neighbours += grid[row+a][col-1]
            if a != 0:
                neighbours += grid[row+a][col]
            if col+1 < len(grid[row+a]):
                neighbours += grid[row+a][col+1]

    return neighbours


if __name__ == '__main__':
    #~ #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

