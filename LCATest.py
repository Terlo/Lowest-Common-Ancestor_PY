import unittest
from LCA import Node
from LCA import LCA


class LowestCommonAncestorTest(unittest.TestCase):




    def testRootNode(self):
        a = Node(0)
        b = Node(1)
        c = Node(2)
        d = Node(0)
        e = Node(1)
        a.left = b
        a.right= c
        b.left = d 
        b.right = e
#test the case where the root is the LCA between the two nodes
        obj = LCA()
        result = obj.LowestCommonAncestor(c,b,a)
        self.assertEqual(a, result)

    def testNoLCA(self):
        a = Node(0)
        b = Node(1)
        c = Node(2)
        d = Node(0)
        e = Node(1)
        f = Node(1)
        a.left = b
        a.right= c
        b.left = d 
        b.right = e
#test the scenario where there exists two nodes which have no lca
        obj = LCA()
        result = obj.LowestCommonAncestor(c,f,a)
        self.assertEqual(None, result)


    def testNodeIsLCA(self):
        a = Node(0)
        b = Node(1)
        c = Node(2)
        d = Node(0)
        e = Node(1)
        a.left = b
        a.right= c
        b.left = d 
        b.right = e
#test the case where one of the selected nodes is the lca
        obj = LCA()
        result = obj.LowestCommonAncestor(d,b,a)
        self.assertEqual(b, result)
        

    def testIsEmpty(self):
        a = Node(0)
        b = Node(1)
        c = Node(2)
        d = Node(0)
        e = Node(1)
        a.left = b
        a.right= c
        b.left = d 
        b.right = e
#test the case where the tree is empty
        obj = LCA()
        result = obj.LowestCommonAncestor(c,b,None)
        self.assertEqual(None, result)
  

  
if __name__ == '__main__':
    unittest.main()