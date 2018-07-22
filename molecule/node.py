class Node(object):
    neighbors = None
    content   = ''

    def __init__(self, neighbors = [], content = ''):
        try:
            self.neighbors = set(neighbors)
            for n in neighbors:
                n.add(self)
        except AttributeError:
            self.neighbors = set([])

        try:
            self.neighbors.remove(self)
        except KeyError:
            pass

        self.content   = content

    def add(self, neighbor):
        if not (neighbor is self):
            self.neighbors.add(neighbor)

    def list_neighbors(self, exclude = []):
        s = ''
        for n in self.neighbors:
            if not (n in exclude):
                s += '%s ' % n.content

        return s

    # def to_string(self, exclude):
    #     for neighbor in self.neighbors:
    #         print neighbor.content
    #         if not (neighbor in exclude):
    #             return '%s -> %s' % (self.content, self.list_neighbors(exclude))
    #     return self.content
    #
    # def search(self, item, exclude = []):
    #     if item in self.neighbors:
    #         return self.content
    #     # if self.neighbors in exclude:
    #     #     return self
    #     for n in self.neighbors:
    #         print n.content
    #         if not (n in exclude):
    #             return n.search(item, [exclude, self])

# a = Node([], 'a')
# b = Node([a], 'b')
# c = Node([b], 'c')
# d = Node([b], 'd')
# e = Node([c], 'e')
#
# print d.search(e)

# print d.list_neighbors()
# print d.to_string([])
