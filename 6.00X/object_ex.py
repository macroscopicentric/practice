class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        #compares two sets and makes a new set of the overlap
        overlap = intSet()
        for number in self.vals:
            if number in other.vals:
                overlap.insert(number)
        return overlap 

    def __len__(self):
        #gets length of self
        return len(self.vals)

first = intSet()
first.insert(1)
second = intSet()
second.insert(1)
third = intSet()

print first.intersect(second)
print second.intersect(third)
print first.__len__()
