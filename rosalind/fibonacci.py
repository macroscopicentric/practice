# 1, 1, 2, 3, 5, 8, 13, 21, 34

a = 1
b = 1
c = 0

seq = [a, b]
print seq

for num in range(2, 5):
    c = 4 * a + b
    a = b
    b = c
    seq.append(b)
    print seq
    num += 1