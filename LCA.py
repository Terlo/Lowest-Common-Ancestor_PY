from py_compile import main

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



_result = Node(0)
p = Node(0)
q=  Node(0)
   
def LowestCommonAncestor(p, q, root):
    if root == None:
        return None
    left =False
    right = False
    current = False

    left = LowestCommonAncestor(root.left,p,q)
    right =LowestCommonAncestor(root.right,p,q)
    current =  (root == p or root == q)
    if (right and left) or (left and current) or (right and current):
        return root
    return right or left or current
    


def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    print("running the lca function")
    LowestCommonAncestor(a, d, g)
        

main()
print(f"LOWEST COMMON ANCESTOR FOR NODE{int} and node {int} is {int}",p.val,q.val,_result.val)






    

