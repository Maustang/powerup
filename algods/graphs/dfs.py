"""
This is depth first traversal of the graph. As the name suggests we have to
go the the deepest node from the current node and then backtrack back.
Then go to its neighbour and then again traverse to the deepest Node.

Application:
"""
from algods.graphs import graph


def traverse(vertex, visited):
    visited.append(vertex)
    print vertex.label
    for edge in vertex.edges:
        if edge.vertex2 not in visited:
            traverse(edge.vertex2, visited)

def dfs(graph):
    visited = [] 
    # Travese all node as graph can be disconnected
    for vertex in graph.vertices.values():
        if vertex in visited:
            continue
        traverse(vertex, visited)
        
g  = graph.Graph.load_graph("s2")
dfs(g) 