from collections import defaultdict

# A class that represents a directed graph
# using adjacency list representation


class graph:

    def __init__(self):
        '''
        Constructor function
        '''
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        '''
        function to add an edge to graph
        '''
        self.graph[u].append(v)

    def v_visited(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.v_visited(neighbour, visited)

    def dfs_algorithm(self, v):
        visited = set()
        self.v_visited(v, visited)


if __name__ == "__main__":
    g = graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(5, 1)
    g.dfs_algorithm(0)
