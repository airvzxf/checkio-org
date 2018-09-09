def checkio(txt):
    '''
    string with dot separated numbers, which inserted after every third digit from right to left
    '''
    t = ""
    for a in txt.split():
        if a.isdigit():
            m = len(a) // 3
            d = len(a) % 3

            t = t + a[0:d]
            a = a[d:]

            for n in range(m):
                if d != 0: t = t + "."
                if d == 0 and n > 0:  t = t + "."
                t = t + a[n*3:n*3+3]
        else:
            t = t + a
        t = t + " "
    t  = t[0:-1]
    print "t: ",t
    return t

if __name__ == '__main__':
    assert checkio('price is 1') == 'price is 1'
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    print 'All ok'