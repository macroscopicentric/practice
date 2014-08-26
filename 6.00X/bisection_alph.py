def isIn(char, aStr):
    avg = (0 + len(aStr)) // 2 + len(aStr) % 2
    print "aStr: ", aStr
    print "Avg: ", avg
    # if aStr != '' and len(aStr) > 1: print "aStr[avg]: ", aStr[avg]
    print
    if aStr == '':
        return False
    elif aStr[avg] == char or (len(aStr) == 1 and aStr == char):
        print "Error"
        return True
    else:
        if aStr[avg] > char:
            aStr = aStr[:avg]
            isIn(char, aStr)
        else:
            aStr = aStr[avg:]
            isIn(char, aStr)
            

string_ex = 'abcdeflmnop'
print isIn('f', string_ex)
# print isIn('a', '')

#Bugs: even vs. odd? return True not working (returns None). Has difficulties with letters that aren't in the string.