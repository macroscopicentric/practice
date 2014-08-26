def summation(num_list):
    if num_list == []:
        return 0
    else: return num_list[0] + summation(num_list[1:])

print summation([1, 2, 3, 4, 5])

print summation([])