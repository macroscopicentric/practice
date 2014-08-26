dataset = """
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""

dataset = dataset.split('\n')
dataset.pop(0)
dataset1 = dataset.pop(0)
dataset2 = dataset.pop(0)

total = 0

def string_test(dataset1, dataset2):
    global total
    if len(dataset1) != 0:
        if dataset1[0] == dataset2[0]: pass
        else: total += 1
        dataset1 = dataset1[1:]
        dataset2 = dataset2[1:]
        return string_test(dataset1, dataset2)
    else:
        return total


print string_test(dataset1, dataset2)