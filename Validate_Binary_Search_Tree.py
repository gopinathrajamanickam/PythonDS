# Validate a Binary search Tree
# Given a root node of a Tree check if it forms a binary search tree
# A BST is a special tree where for each node
# the left node is less than root node and all
# the right node is greater than root node
'''
         5
      3      7
    2   4  6   8

2 

'''

# Edge cases
# No element
# 1 element
# 2 elements , left , right 
# 3 elements
# 3+ elements 


# Naive solution would be to check each node.
# if node is None return True
# else if left node < 
# 


class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
def isBSTUtil(node,prev):
    # This is a recursion problem
    # Also use in order traversal to validate
             
    # base case
    if node != None:
        print('Step 1')
        if isBSTUtil(node.left,node) == True:
        
            if prev != None and node.val < prev.val:
                print('Step 3')
                return False

        prev = node
        return isBSTUtil(node.right,node)

    print('Step 4')
    return True 
            
    # recursion case
    # set parameter of recursion case towards base case 
    

def isBST(node):
    # Empty Tree  
    if node == None:
        return False
    
    prev = None
    return isBSTUtil(node,prev)
    
        
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)
    
    print(isBST(root))


    
    
