from Queue import Queue
from algods.graphs import graph

"""
1) start with the node and traverse all its neighbours. Put them to a queue

Applications:
"""

def bfs(graph):
    visited = []
    q = Queue()
    for vertex in graph.vertices.values():
        print "start vertex : %s" % vertex.label
        if vertex not in visited:
            q.put(vertex)
        
        while not q.empty():
            v = q.get()
            print v.label
            visited.append(v)
            for edge in v.edges:
                if edge.vertex2 not in visited:
                    visited.append(edge.vertex2) 
                    q.put(edge.vertex2)
                    

g  = graph.Graph.load_graph("s2")
bfs(g) 