import timeit
import profile

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def buildGraphOriginal(wordFile):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    with open(wordFile) as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def buildGraphListComp(wordFile):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    with open(wordFile) as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        [g.addEdge(word1, word2) for word1 in d[bucket] for word2 in d[bucket] if word2 != word1]
    return g

def buildGraphFunctional(wordFile):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    with open(wordFile) as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        map(g.addEdge, filter(lambda x: x[0] != x[1], zip(d[bucket], d[bucket])))
    return g

def buildGraphSlice(wordFile):
    d = {}
    g = Graph()
    enum = enumerate
    # create buckets of words that differ by one letter
    with open(wordFile) as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for index, word1 in enum(d[bucket]):
            for word2 in d[bucket][index:]:
                    g.addEdge(word1,word2)
    return g

def buildGraphRecurse(wordFile):
    d = {}
    g = Graph()
    # create buckets of words that differ by one letter
    with open(wordFile) as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    def buildHelper(bucket):
        if bucket == []:
            return None
        else:
            word1 = bucket[0]
            [g.addEdge(word1, word) for word in bucket[1:]]
            buildHelper(bucket[1:])
    for bucket in d.keys():
        buildHelper(d[bucket])
    return g

sowpods = '../recursion/sowpods.txt'
print "buildGraphOriginal: %s seconds." % (round(timeit.timeit('buildGraphOriginal(sowpods)', setup='from __main__ import buildGraphOriginal, sowpods', number=1), 2))
# print "buildGraphListComp: %s seconds." % (round(timeit.timeit('buildGraphListComp(sowpods)', setup='from __main__ import buildGraphListComp, sowpods', number=1), 2))
print "buildGraphFunctional: %s seconds." % (round(timeit.timeit('buildGraphFunctional(sowpods)', setup='from __main__ import buildGraphFunctional, sowpods', number=1), 2))
# print "buildGraphSlice: %s seconds." % (round(timeit.timeit('buildGraphSlice(sowpods)', setup='from __main__ import buildGraphSlice, sowpods', number=1), 2))
# print "buildGraphRecurse: %s seconds." % (round(timeit.timeit('buildGraphRecurse(sowpods)', setup='from __main__ import buildGraphRecurse, sowpods', number=1), 2))

#addNeighbor = unidirectional, so need for loop to add in both directions. Therefore slicing and recursive solutions above are wrong.
#Amber's hypothesis: slicing = copying (costly), which is why those versions were slower anyway.

# print "buildGraphOriginal: %s" % (profile.run('buildGraphOriginal(sowpods)'))
# print "buildGraphRecurse: %s" % (profile.run('buildGraphRecurse(sowpods)'))

# for vertex in graph:
#     print vertex

# def bfs(g,start):
#   start.setDistance(0)
#   start.setPred(None)
#   vertQueue = Queue()
#   vertQueue.enqueue(start)
#   while (vertQueue.size() > 0):
#     currentVert = vertQueue.dequeue()
#     for nbr in currentVert.getConnections():
#       if (nbr.getColor() == 'white'):
#         nbr.setColor('gray')
#         nbr.setDistance(currentVert.getDistance() + 1)
#         nbr.setPred(currentVert)
#         vertQueue.enqueue(nbr)
#     currentVert.setColor('black')





