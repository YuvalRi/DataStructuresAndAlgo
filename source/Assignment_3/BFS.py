from collections import defaultdict

# A class that represents a directed graph
# using adjacency list representation


class graph:

    def __init__(self):
        '''
        Constructor function
        '''
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        '''
        A function that adds an edge to graph
        '''
        self.graph[u].append(v)

    def bfs_algorithm(self, s):
        '''
        A function which prints a BFS of graph
        '''
        # mark all the vertices as not visited
        visited = [False]*(max(self.graph) + 1)
        # create a queue for BFS
        queue = []
        # mark the souce node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            # dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")
            # get all adjacent vertices of dequeued vertex s.
            # if a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("Following is Breadth First Traversal") #starting from vertex 2
    g.bfs_algorithm(2)

