def laceStrings(s1, s2):
    s1_length = 0
    s2_length = 0
    string_marker = 's2'
    new_string = ''

    if s1 == '' and s2 == '':
        return new_string

    while s1_length < len(s1) and s2_length < len(s2):
        if string_marker == 's2':
            new_string += s1[s1_length]
            s1_length += 1
            string_marker = 's1'
        else:
            new_string += s2[s2_length]
            s2_length += 1
            string_marker = 's2'
    if s1_length < len(s1):
        new_string += s1[s1_length:]
    else:
        new_string += s2[s2_length:]
    return new_string

print laceStrings('', '')
print laceStrings('', 'fghij')
print laceStrings('abcde','')
print laceStrings('abcd', 'efghi')
print laceStrings('ac', 'b')