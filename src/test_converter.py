from unittest import TestCase, main

from converter import text_node_to_html_node
from textnode import TextNode, TextType



class converterTest(TestCase):

    def test_convert_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.value, "This is a text node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
    def test_convert_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "This is a bold node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
    def test_convert_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.tag, "i")
            self.assertEqual(html_node.value, "This is a italic node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
    def test_convert_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.tag, "code")
            self.assertEqual(html_node.value, "This is a code node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
    def test_convert_link(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.tag, "a")
            self.assertEqual(html_node.value, "This is a link node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
        
    def test_convert_image(self):
        node = TextNode("This is a image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        if html_node: 
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "This is a image node")
        else:
            raise TypeError("text_node_to_html_node fails to convert text node")
        

if __name__ == "__main__":
    main()