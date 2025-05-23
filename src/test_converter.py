from unittest import TestCase, main

from converter import extract_markdown_images, split_nodes_delimiter, text_node_to_html_node
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
    
    def test_split_node_delimiter_end_with_delimiter(self):

        node = TextNode("`This is a code block`",TextType.TEXT)
        split_array = split_nodes_delimiter([node],"`",TextType.CODE)
        ans = "TextNode(This is a code block, code_text, None)"
        self.assertEqual(repr(split_array[0]), ans )
    def test_split_node_delimiter_between_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        # self.assertEqual(new_nodes[0],TextNode("This is text with a ", TextType.TEXT))
        # self.assertEqual(new_nodes[1],TextNode("code block", TextType.CODE))
        # self.assertEqual(new_nodes[2],TextNode(" word", TextType.TEXT))

        ans = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(ans,new_nodes)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
if __name__ == "__main__":
    main()