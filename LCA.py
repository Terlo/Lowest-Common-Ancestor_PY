from py_compile import main

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None




class LCA:
    def LowestCommonAncestor(self,p:'Node',q:'Node', root:'Node') -> 'Node':
        self.result= None 

        def search(node):
            if not node:
                return False
            left = search(node.left)
            right = search(node.right)
            current = node==p or node ==q
            if (left and right) or (current and right) or (current and left):
                self.result = node
                return
            return left or right or current
        search(root)
        return self.result            

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    # d = Node(4)
    # e = Node(5)
    # f = Node(6)
    # g = Node(7)

    a.left = b
    a.right = c 

    lcatest= LCA()

    print("running the lca function")
    result = lcatest.LowestCommonAncestor(c, b, a)

    print(f"the lca is {result.val}")
        

main()







    

