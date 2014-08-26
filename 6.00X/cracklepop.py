for n in range(0, 101):
    if n % 3 == 0 and n % 5 == 0: print "CracklePop"
    elif n % 5 == 0: print "Pop"
    elif n % 3 == 0: print "Crackle"
    else: print n