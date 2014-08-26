def laceStringsRecur(s1, s2):
    def helpLaceStrings(s1, s2, out):
            if s1 == '':
                return out + s2
            if s2 == '':
                return out + s1
            else:
                return helpLaceStrings(s2, s1[1:], out + s1[0])
    return helpLaceStrings(s1, s2, '')

print laceStringsRecur('', '')
print laceStringsRecur('', 'fghij')
print laceStringsRecur('abcde','')
print laceStringsRecur('abcd', 'efghi')
print laceStringsRecur('ac', 'b')