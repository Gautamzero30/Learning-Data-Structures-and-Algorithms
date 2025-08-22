from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # undirected graph

    def print_graph(self):
        for node in range(self.V):
            print(node, "->", self.adj[node])

# Example
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
