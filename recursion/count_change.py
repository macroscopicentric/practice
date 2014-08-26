def count_change(amt, denoms):
    if denoms == []:
        return 0
    elif amt < 0:
        return 0
    elif amt == 0:
        return 1
    else:
        return count_change(amt - denoms[-1], denoms) + count_change(amt, denoms[:-1])