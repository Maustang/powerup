import os
import imp


class Node():
    def __init__(self, data=None,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right
        
        


def create_tree(file_name=None, par='A'):
    samples_dir_path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
    sample_file_path =  os.path.join(samples_dir_path, "%s.py" % file_name)
    module_obj = imp.load_source(file_name, sample_file_path)
    tree_dict = module_obj.T

    nodes_obj = {}
    for parent in tree_dict:
        left_child = tree_dict[parent][0]
        try:
            right_child = tree_dict[parent][1]
        except IndexError:
            right_child = None
            right_child_obj = None

        left_child_obj = (nodes_obj[left_child] if left_child in nodes_obj
                          else Node(left_child))
        nodes_obj[left_child] = left_child_obj

        if right_child:
            right_child_obj = (nodes_obj[right_child] if right_child in nodes_obj
                               else Node(right_child))
            nodes_obj[right_child] = right_child_obj

        if parent in nodes_obj:
            parent_obj = nodes_obj[parent]
            parent_obj.left = left_child_obj
            parent_obj.right = right_child_obj
        else:
            parent_obj = Node(parent, left_child_obj, right_child_obj)
            nodes_obj[parent] = parent_obj

    #for node in nodes_obj:
    #    print nodes_obj[node]

    return nodes_obj[par]


def print_tree(root):
    q = []
    q.append(root)
    q.append(None)
    level =0
    while q:
        node = q.pop(0)
        if node == None and not q:
            break
        if node==None:
            print "\n"
            q.append(None)
            level = level + 1
            continue
        print node.data,
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

if __name__ == '__main__':
    t = create_tree('t1')
    print_tree(t)