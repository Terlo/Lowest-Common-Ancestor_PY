from py_compile import main

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



_result = Node(0)

def LowestCommonAncestor(p, q, root):
    root = Node()
    if not root:
        return None
    print(f"LOWEST COMMON ANCESTOR FOR NODE{int} and node {int} is {int}",p.val,q.val,)
    current = Node()
    left = LowestCommonAncestor(root.left,p,q)
    right =LowestCommonAncestor(root.right,p,q)
    current =  (root.val == p or root.val  == q)
    if right and left:
        return root
    if left and current:
        return root
    if right and current:
        return root
    return right or left or current
    


def main():
    a = Node(val=1)
    b = Node(val=2)
    c = Node(val=3)
    d = Node(val=4)
    e = Node(val=5)
    f = Node(val=6)
    g = Node(val=7)

    LowestCommonAncestor(a, d, g);
        






    

