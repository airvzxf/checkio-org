op = {'+':2, '-':2, '/':3, '*':3, '^':4, '(':0, ')':5}
def checkio(e):
    r = list()
    o = list()
    for x in range(len(e)):
        z = ord(e[x])
        if z in range(48, 58) or z in range(65, 91) or z in range(97, 123):
            r.append(e[x])
        else:
            o.append(e[x])
            if len(o)>1:
                o_max = len(o)-1
                if op[o[o_max]] < op[o[o_max-1]] or op[o[o_max]] == 5:
                    if op[o[o_max]] != 0:
                        r.append(o[o_max-1])
                        o.pop(o_max-1)
                        o_max = len(o)-1
                        for x2 in range(len(o)-2, -1, -1):
                            if o[x2] == "(":
                                break
                            r.append(o[x2])
                            o.pop(x2)
                            o_max = len(o)-1
                    if op[o[o_max]] == 5:
                        o.pop(o_max)
                        for x2 in range(len(o)-1, -1, -1):
                            if o[x2] == "(":
                                o.pop(x2)
                                break
    for x2 in range(len(o)-1, -1, -1):
        r.append(o[x2])
        o.pop(x2)
    re = ''.join(r)
    # print "#################"
    # print "e : ", e
    # print "re: ", re
    return re

if __name__ == '__main__':
    assert checkio("(a+(b*c))") == "abc*+", "1"
    assert checkio("((a+b)*(z+x))") == "ab+zx+*", "2"
    assert checkio("((a+t)*((b+(a+c))^(c+d)))") == "at+bac++cd+^*", "3"
    assert checkio('a+b*c+d') == 'abc*+d+', "3"

    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'

    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'
    print '**************************** All ok ****************************'