#Stack/moveTower() code from Algorithms/Data Structures. hanoi() based on http://www.python-course.eu/towers_of_hanoi.php.

class Stack(object):
    def __init__(self, name):
        self.items = []
        self.name = name

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def hanoi(height):
    fromPole = Stack('fromPole')
    #To reverse numbers:
    for num in range(height, 0, -1):
        fromPole.push(num)
    toPole = Stack('toPole')
    withPole = Stack('withPole')
    def hanoi_helper(n, source, helper, target):
        if n > 0:
            hanoi_helper(n-1, source, target, helper)
            if not source.isEmpty():
                current = source.pop()
                target.push(current)
                print "Moving %s from %s to %s." % (current, source.name, target.name)
                print "%s %s %s" % (withPole.items, fromPole.items, toPole.items)
            hanoi_helper(n-1, helper, source, target)
    hanoi_helper(fromPole.size(), fromPole, withPole, toPole)


hanoi(5)

# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)

# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)

# moveTower(3,"A","B","C")