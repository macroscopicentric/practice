def isIn(char, aStr):
    avg = len(aStr) / 2
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif aStr[avg] == char:
        return True
    elif aStr[avg] > char:
        return isIn(char, aStr[:avg])
    elif aStr[avg] < char:
        return isIn(char, aStr[avg:])
    else: return "Error"
            

string_ex = 'abcdeflmnop'
print "f is in %s: " % string_ex, isIn('f', string_ex)
print "c is in %s: " % string_ex, isIn('c', string_ex)
print "l is in %s: " % string_ex, isIn('l', string_ex)
print "g is in %s: " % string_ex, isIn('g', string_ex)
print "a is in '': ", isIn('a', '')
print "a is in 'a': ", isIn('a', 'a')
print "a is in 'b': ", isIn('a', 'b')