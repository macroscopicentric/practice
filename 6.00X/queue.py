class Queue(object):
    def __init__(self):
        self.ints = []

    def insert(self, number):
        self.ints.insert(0, number)

    def remove(self):
        try: return self.ints.pop()
        except: raise ValueError()

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()