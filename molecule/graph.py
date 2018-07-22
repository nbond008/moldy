from node import Node

class Graph(object):
    nodes     = []
    dead_ends = []
    id    = ''

    def __init__(self, head, id):
        self.map(head, [head])

        self.id = id
        if not id:
            self.id = head.content

    def map(self, node, visited = []):
        unique = False
        if node not in visited:
            visited.append(node)

        nb = list(node.neighbors)
        nb.append(node)

        for n in nb:
            if not (n in visited):
                unique = True

        if len(node.neighbors) == 1 and not (node in self.dead_ends):
            self.dead_ends.append(node)
            unique = False

        self.nodes.append(node)
        for n in node.neighbors:
            if self.nodes.count(n) < len(n.neighbors) and unique:
                self.map(n, nb)

        # new_nodes = []
        # for m in self.nodes:
        #     if m not in new_nodes:
        #         new_nodes.append(m)
        #
        # self.nodes = new_nodes


a = Node([], 'a')
b = Node([a], 'b')
c = Node([b], 'c')
d = Node([c], 'd')
e = Node([a, d], 'e')
f = Node([a], 'f')
g = Node([c], 'g')
h = Node([a], 'h')

molecule = Graph(a, 'test')

# print '\n'
#
# new_nodes = []
# for m in molecule.nodes:
#     if m not in new_nodes:
#         new_nodes.append(m)
#
# molecule.nodes = new_nodes

for n in molecule.nodes:
    print n.content
