import math

def getNoPermutaciones(n=0, lvl=1):
    if lvl == n+1:
        return False
    a = math.factorial(n)
    b = math.factorial(n-lvl)
    return int(a/b) + getNoPermutaciones(n, lvl+1)
    pass

def formatPermutaciones(l=list(), n=0):
    m = getNoPermutaciones(n)
    o = int(m/n)
    for x in range(n):
        print l[x*o:x*o+o]
        print ""
    pass

def generarRepeticiones(li=list(), p=list(), lvl=0, l=list(), r=list()):
    if len(li) == 1:
        return li
    if lvl == 0:
        p = []
        r = list(li)
    l_tmp = list(l)
    r_tmp = list(r)
    for i in range(len(li)-lvl):
        l = list(l_tmp)
        l.append(r_tmp[i])
        r = list(r_tmp)
        r.pop(i)
        p.append([l,r])
        generarRepeticiones(li, p, lvl+1, list(l), list(r))
    return p

def checkio(stones):
    print "Stones: ", stones
    p = generarRepeticiones(stones)
    if len(p) == 1:
        print ""
        return p[0]
    print p
    print "Total de permutaciones: ", len(p)
    print "Posibles permutaciones: ",getNoPermutaciones(len(stones))
    #formatPermutaciones(p, len(stones))
    s = list()
    l,r = p[0]
    m = int(math.fabs(math.fsum(l)-math.fsum(r)))
    for x in range(len(p)):
        l,r = p[x]
        a = int(math.fsum(l))
        b = int(math.fsum(r))
        n = int(math.fabs(a-b))
        if n < m:
            s = list()
            m = n
        if n == m:
            s.append(p[x]) 
    #return m, s
    return int(m)


if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'