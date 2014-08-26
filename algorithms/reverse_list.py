def reverse_list(orig_list):
    if len(orig_list) == 0:
        return []
    else:
        return [orig_list[-1]] + reverse_list(orig_list[:-1])

print reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])