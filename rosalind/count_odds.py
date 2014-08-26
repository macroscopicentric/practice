a = input("A:")
b = input("B:")

count = 0

for i in range(a,(b + 1)):
    global count
    if i % 2 != 0:
        count += i

print count

# n = 10
# for i in range(n):
#   print i

# print range(5, 12)