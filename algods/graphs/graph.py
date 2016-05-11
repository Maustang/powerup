import os
import imp


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
        
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def __str__(self):
        return self.label
        
        
class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight 


class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.vertices = {}
    
    def add_edge(self, vertex1_label, vertex2_label, weight=0):
        if vertex1_label in self.vertices:
            vertex1 = self.vertices[vertex1_label]
        else:
            vertex1 = Vertex(vertex1_label)
            self.vertices[vertex1_label] = vertex1
        
        if vertex2_label in self.vertices:
            vertex2 = self.vertices[vertex2_label]
        else:
            vertex2 = Vertex(vertex2_label)
            self.vertices[vertex2_label] = vertex2
        
        edge = Edge(vertex1, vertex2, weight)
        vertex1.add_edge(edge)
        if not self.directed:
            edge = Edge(vertex2, vertex1, weight)
            vertex2.add_edge(edge)
    
    def print_graph(self):
        for vertex in self.vertices:
            print vertex,
            for edge in self.vertices[vertex].edges:
                print "( %s %s )" % (edge.vertex2, edge.weight),
            print
    
    @classmethod        
    def load_graph(cls, file_name):
        samples_dir_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
        sample_file_path =  os.path.join(samples_dir_path, "%s.py" % file_name)
        module_obj = imp.load_source(file_name, sample_file_path)
        graph_dict = module_obj.G
        graph = cls()
        for vertex in graph_dict:
            for edge in graph_dict[vertex]:
                graph.add_edge(vertex, edge)
        return graph
