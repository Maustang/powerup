from algods.trees import node



def inorder(root):
    """
    Left , Node and Right
    """
    if not root:
        return
    
    inorder(root.left)
    print root.data + " ",
    inorder(root.right)
    

def preorder(root):
    """
    Node, Left, Right
    """
    if not root:
        return
    
    print root.data + " ",
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    "Left, Right, Node"
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.data + " ",


if __name__ == '__main__':
    
    tree  = node.create_tree('t1')
    inorder(tree)
    print
    preorder(tree)
    print
    postorder(tree)
    
    