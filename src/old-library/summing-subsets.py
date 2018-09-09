import itertools

def f(n):
    t = 0
    for nt in range(1, n+1):
        for c in itertools.combinations(range(1,n+1), nt):
            t = t + sum(c)
    return t
def checkio(n):
    '''
    Let G(S) denote the sum of the elements of set S and F(n) be the sum of G(s) 
    for all subsets of the set consisting of the first n natural numbers. 
    For example, F(3) = (1) + (2) + (3) + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24. 
    Given n, calculate F(1) + F(2) + ... + F(n)
    '''
    t = 0
    for nt in range(1,n+1):
        t = t + f(nt)
    return t

if __name__ == '__main__':
    assert checkio(1) == 1, "1"
    assert checkio(2) == 7, "2"
    assert checkio(3) == 31, "3"
    assert checkio(4) == 111, "4"
    print 'All ok'