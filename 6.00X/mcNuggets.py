def mcNuggets(n):
    a = 0
    b = 0
    c = 0

    if n < 6:
        return False

    while 6 * a + 9 * b + 20 * c <= n:
        print a, b, c
        if 6 * a + 9 * b + 20 * c == n:
            return True
        elif n - 20 * c >= 20:
            if (n - (c + 1) * 20) % 9 == 0 or (n - (c + 1) * 20) % 6 == 0:
                pass
            else:
                c += 1
        elif n - 20 * c - 9 * b >= 9:
            if (n - c * 20 + (b + 1) * 9) % 6 == 0:
                pass
            else:
                b +=1
        elif n - 20 * c - 9 * b - 6 * a >= 6:
            a += 1
        else:
            return False

print mcNuggets(52)
print mcNuggets(12)
print mcNuggets(21)
print mcNuggets(24)