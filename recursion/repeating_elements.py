"""
How do you test whether there are repeating elements in a list?
"""
#Brute force-- O(n^2)
def test_repeat(letters):
    for a in letters:
        for b in letters:
            if a == b:
                return False
    return True

#First try-- O(n log n)-- the time for sorting
letters.sort() == list(set(letters)).sort()

#More efficient, don't need to do the sorting-- O(n)
len(letters) == len(set(letters))

#What if we wanted to make it optimistic, so can usually do better than O(n)?-- O(n) but better than above
def test_repeat(letters):
    letters_set = set()
    for letter in letters:
        if letter in letters_set:
            return False
        else:
            letters_set.add(letter)
    return True

#If you know the length of the list of possible characters, you could also do a quick check to see if your list is longer than that. Ie, if you're testing a list that's only filled with lowercase letters, there can't be more than 26 of them or something is overlapping.