import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_create_leafNode_sucess(self):
        node = LeafNode("p", "This is a paragraph", None, None)
        return isinstance(node, LeafNode) and self.assertEqual(repr(node), "LeafNode(p, This is a paragraph, None)")
    
    def test_create_leafNode_fail(self):
        node2 = LeafNode("p", "This is a paragraph", None, None)
        with self.assertRaises(ValueError):
            node = LeafNode("p", "This is a paragraph", [node2], None)
        # return isinstance(node, LeafNode) and self.assertEqual(repr(node), "tag: p value:This is a paragraph children:None props:None")
   
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
if __name__ == "__main__":
    unittest.main()