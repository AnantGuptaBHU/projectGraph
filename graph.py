#https://www.geeksforgeeks.org/find-k-cores-graph/
from collections import defaultdict
class Graph():
    def __init__(self,total_vertices):
        self.graph=defaultdict(list)
        self.TV=total_vertices
    def addEdge(self,src,dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)
    def K_cores(self,k):
        k_array=[False]*self.TV
        q=[]
        for src,dest_list in self.graph.items():
            if len(dest_list)<k:
                q.append(src)
                k_array[src]=True
        while len(q)!=0:
            popped_vertex=q.pop(0)
            while len(self.graph[popped_vertex])!=0:
                dest=self.graph[popped_vertex][0]
                self.graph[popped_vertex].remove(dest)
                self.graph[dest].remove(popped_vertex)
                if len(self.graph[dest])<k and k_array[dest]==False:
                    q.append(dest)
                    k_array[dest]=True
    def print_vertex_with_edges(self):
        for src,dest_list in self.graph.items():
            if len(self.graph[src])!=0:
                print(src,"-->",dest_list)

g1 = Graph(9)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
print("before removal k cores")
g1.print_vertex_with_edges()
print("after removal k cores")
g1.K_cores(3)
g1.print_vertex_with_edges()