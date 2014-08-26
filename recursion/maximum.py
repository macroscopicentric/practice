def maximum(numbers, largest_so_far=0):

    if numbers == []:

        return largest_so_far

    next_num = numbers[0]

    return maximum(numbers[1:], max(next_num, largest_so_far))

print maximum([53, 85, 49, 15, 50, 17, 75, 6, 39, 99, 38, 89, 27, 82, 95, 62, 51, 42, 3,
    27])