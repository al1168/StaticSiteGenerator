# from unittest import TestCase
import unittest
from htmlnode import HTMLNode
""" 
<div>
 <p>
    This could be a cool project
 </p>
</div>

"""
class HTMLNodeTest(unittest.TestCase):
        
    def test_props_to_html(self):
        lnode = HTMLNode("link", None, None,{"href":"https://www.google.com", "target":"_blank"})
        self.assertEqual(lnode.props_to_html(), 'href="https://www.google.com" target="_blank"')
    def test_props_to_html_(self):
        lnode = HTMLNode("link", None, None,{"href":"hm", "target":"_blank"})
        self.assertNotEqual(lnode.props_to_html(), 'href="https://www.google.com" target="_blank"')
    def test_props_to_html_matching(self): 
        lnode = HTMLNode("link", None, None,{"href":"hm","href":"hm"})
        self.assertEqual(lnode.props_to_html(), 'href="hm"')
    # def test_props_to_html(self):
    #     pnode = HTMLNode("p","This could be a cool project",None, None)
    #     divNode = HTMLNode("div",None,[pnode], None)

    #     res = divNode.props_to_html()
    #     self.assertEqual(res,None )
    #     print(res)


if __name__ == "__main__":
    unittest.main()
