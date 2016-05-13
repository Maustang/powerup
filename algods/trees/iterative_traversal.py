from algods.trees import node


def preorder1(root):
    """
    process node, then traverse left and then right
    
    Method 1:
    push the root to stack
    while stack is not empty
        get node from stack
        print/process it
        push its right child
        push its left child
    """
    
    if not root:
        return
    
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        print node.data + " ",
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        

def preorder2(root):
    """
    Method 2:
    
    process node and push itself to  the stack
    go to nodes left
    repeat above until left exists
    if node becomes None ie left subtree is over
        pop the node
        switch to right subtree
    """
    
    stack = []
    node = root
    while node or stack:
        if node:
            print node.data + " ",
            stack.append(node)
            node = node.left
        else:
            #left subtree is over switch to right subtree"
            node = stack.pop()
            node = node.right
    
    
def inorder(root):
    """
    Same as preorder2 
    
    push node to stack
    move to its left until None
    once it reaches the leftmost node pop the node
    print its data
    move to the right
    """
    
    stack = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.data + " ",
            node = node.right
            

def postorder1(root):
    """ 
    Uses 1 stack and visited set
    
    push node into the stack
    move to left until None is encountered
    when leftmost node comes then
    pop the element from stack
    check if it is in visited
    if it is not visited then it means the its coming back from left and not from right
    so push it again on the stack and add to visited set
    move to its right subtree
    repeat
    node comes back again and check if it is in visited
    It yes then its from right and then print the node
    """
     
    stack = []   
    visited = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.append(node)
                node = node.right
            else:
                print node.data + " ",     
                node = None 


def postorder2(root):
    """
    using 2 stacks
    
    postorder(LRN) is same as reverse of preorder ( NRL) with
    right subtree processed before left subtree
    """
    
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    while stack2:
        print stack2.pop().data + " ",

 
if __name__ == '__main__':
    tree  = node.create_tree('t1')
    #preorder1(tree)
    #print
    #preorder2(tree)
    #print
    #inorder(tree)
    print
    postorder1(tree)
    print
    postorder2(tree)