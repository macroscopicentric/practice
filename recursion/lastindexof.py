def lastIndexOf(n, num_list, incrementer=0, last_location=-1):
    if n not in num_list:
        return last_location
    else:
        if num_list[0] == n:
            last_location = incrementer
        return lastIndexOf(n, num_list[1:], incrementer + 1, last_location)

print lastIndexOf(5, [1, 2, 4, 6, 5, 2, 7])

print lastIndexOf(5, [1, 2, 4, 6, 2, 7])

print lastIndexOf(5, [1, 2, 5, 4, 6, 5, 2, 7])