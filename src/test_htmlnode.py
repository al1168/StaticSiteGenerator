# import unittest
# from htmlnode import HTMLNode, ParentNode
# from leafnode import LeafNode
# """ 
# <div>
#  <p>
#     This could be a cool project
#  </p>
# </div>

# """
# class HTMLNodeTest(unittest.TestCase):
        
#     def test_props_to_html(self):
#         lnode = HTMLNode("link", None, None,{"href":"https://www.google.com", "target":"_blank"})
#         self.assertEqual(lnode.props_to_html(), 'href="https://www.google.com" target="_blank"')
#     def test_props_to_html_(self):
#         lnode = HTMLNode("link", None, None,{"href":"hm", "target":"_blank"})
#         self.assertNotEqual(lnode.props_to_html(), 'href="https://www.google.com" target="_blank"')
#     def test_props_to_html_matching(self): 
#         lnode = HTMLNode("link", None, None,{"href":"hm","href":"hm"})
#         self.assertEqual(lnode.props_to_html(), 'href="hm"')

# class ParentNodeTest(unittest.TestCase):

#     """ 
#     happy case: 1 layer nested tags 
#     fail case: single node no children
#     fail case: 1 layer nested parent with no tag
#     happy case2: 2 layer nested tags
#     """
#     def test_one_layer_nest(self):
#         leafnode = LeafNode("p","This is for the Parent Node Test", None, None)         
#         parentnode = ParentNode("div",None,[leafnode],None)
#         self.assertEqual(parentnode.to_html(),"<div><p>This is for the Parent Node Test</p></div>")

#     def test_no_children(self):
#         # no children 
#         with self.assertRaises(ValueError):
#             parentnode = ParentNode("div",None,[],None)

#     def test_no_tag(self):
#         leafnode = LeafNode("p","This is for the Parent Node Test", None, None)         
#         with self.assertRaises(ValueError):
#             parentnode = ParentNode(None,None,[leafnode],None)
    
#     def test_multi_layer_nest(self):
#         # grandfathernode = ParentNode
#         leafnode = LeafNode("p","This is for the Parent Node Test", None, None)         
#         parentnode = ParentNode("div",None,[leafnode],None)
#         grandparentnode = ParentNode("div",None,[parentnode],None)
#         self.assertEqual("<div><div><p>This is for the Parent Node Test</p></div></div>", grandparentnode.to_html())
# if __name__ == "__main__":
#     unittest.main()
