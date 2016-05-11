"""
for every edge (u,v) , u should be visited before v
"""

from algods.graphs import graph

def recurse(vertex, visited, sorted ):
    visited.append(vertex)
    if not vertex.edges:
        sorted.append(vertex)
        return
    
    for edge in vertex.edges:
        if edge.vertex2 not in visited:
            recurse(edge.vertex2, visited, sorted)
        
    # all edges are over push to sorted
    sorted.append(vertex)
        

def topological(graph):
    visited = []
    sorted = []
    for vertex in graph.vertices.values():
        #traverse till the leaf nodes and push the path edges to visited stack
        if not vertex in visited:
            recurse(vertex,visited,sorted)
    #sorted.reverse()
    for i in sorted:
        print i

g  = graph.Graph.load_graph("s2")
topological(g)