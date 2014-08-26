def myLog(x, b):
    if x < 0 or b < 2 or type(x) != int or type(b) != int:
        return None

    log = 0
    while b ** (log + 1) <= x:
        log += 1
    return log

print myLog(0, 0)
print myLog(1, 2.5)
print myLog(1, 2)
print myLog(2, 2)
print myLog(64, 2)