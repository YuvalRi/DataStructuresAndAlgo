# The aim of this algorithm is to find the most
# common degree in a given graph.
# if there is more than one common degree
# return the maximum one.

# from BFS import graph
from collections import defaultdict

# A class that represents a directed graph
# using adjacency list representation


class graph:

    def __init__(self):
        '''
        Constructor function
        '''
        # default dictionary to store graph
        self.graph = {}

    def add_edge(self, u, v):
        '''
        A function that adds an edge to graph
        '''
        self.graph[u].update(v)

    def bfs_algorithm(self, s):
        '''
        A function which prints a BFS of graph
        '''
        # mark all the vertices as not visited
        visited = [False]*(max(self.graph) + 1)
        # create a queue for BFS
        dict = {}
        # mark the source node as visited and enqueue it
        dict.update(s)
        visited[s] = True
        while dict:
            # dequeue a vertex from queue and print it
            s = dict.pop(0)
            print(s, end=" ")
            # get all adjacent vertices of dequeued vertex s.
            # if a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    dict.append(i)
                    visited[i] = True


if __name__ == "__main__":
    # graph = {'1': set(['2', '4', '3']),
    #          '2': set(['1', '4', '6', '7', '8']),
    #          '3': set(['1', '4', '5', '7', '8']),
    #          '4': set(['1', '2', '6', '5', '3']),
    #          '5': set(['4', '3']),
    #          '6': set(['2', '4']),
    #          '7': set(['2', '8', '3']),
    #          '8': set(['2', '7', '3'])}

    # print(graph['1'])
    # print(graph['2'])
    # print(graph['3'])
    # print(graph['4'])
    g = graph()
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(1, 3)
    g.add_edge(2, 1)
    g.add_edge(2, 4)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(2, 8)
    g.add_edge(3, 1)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 7)
    g.add_edge(3, 8)
    g.add_edge(4, 1)
    g.add_edge(4, 2)
    g.add_edge(4, 6)
    g.add_edge(4, 5)
    g.add_edge(4, 3)
    g.add_edge(5, 4)
    g.add_edge(5, 3)
    g.add_edge(6, 2)
    g.add_edge(6, 4)
    g.add_edge(7, 2)
    g.add_edge(7, 8)
    g.add_edge(7, 3)
    g.add_edge(8, 2)
    g.add_edge(8, 7)
    g.add_edge(8, 3)

    print("Following is Breadth First Traversal") #starting from vertex 2
    g.bfs_algorithm(1)
