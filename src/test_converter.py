from unittest import TestCase, main

from converter import extract_markdown_images, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_node_to_html_node, text_to_textnodes
from textnode import TextNode, TextType



class converterTest(TestCase):

    # def test_convert_text(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.value, "This is a text node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
    # def test_convert_bold(self):
    #     node = TextNode("This is a bold node", TextType.BOLD)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.tag, "b")
    #         self.assertEqual(html_node.value, "This is a bold node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
    # def test_convert_italic(self):
    #     node = TextNode("This is a italic node", TextType.ITALIC)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.tag, "i")
    #         self.assertEqual(html_node.value, "This is a italic node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
    # def test_convert_code(self):
    #     node = TextNode("This is a code node", TextType.CODE)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.tag, "code")
    #         self.assertEqual(html_node.value, "This is a code node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
    # def test_convert_link(self):
    #     node = TextNode("This is a link node", TextType.LINK)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.tag, "a")
    #         self.assertEqual(html_node.value, "This is a link node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
        
    # def test_convert_image(self):
    #     node = TextNode("This is a image node", TextType.IMAGE)
    #     html_node = text_node_to_html_node(node)
    #     if html_node: 
    #         self.assertEqual(html_node.tag, "img")
    #         self.assertEqual(html_node.value, "This is a image node")
    #     else:
    #         raise TypeError("text_node_to_html_node fails to convert text node")
    
    # def test_split_node_delimiter_end_with_delimiter(self):

    #     node = TextNode("`This is a code block`",TextType.TEXT)
    #     split_array = split_nodes_delimiter([node],"`",TextType.CODE)
    #     ans = "TextNode(This is a code block, code_text, None)"
    #     self.assertEqual(repr(split_array[0]), ans )
    # def test_split_node_delimiter_between_text(self):
    #     node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    #     ans = [
    #             TextNode("This is text with a ", TextType.TEXT),
    #             TextNode("code block", TextType.CODE),
    #             TextNode(" word", TextType.TEXT),
    #         ]
    #     self.assertEqual(ans,new_nodes)

    # def test_extract_markdown_images(self):
    #     matches = extract_markdown_images(
    #         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    #     )
    #     self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    

    # def test(self):
    #     node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_link([node])
    #     ans = [
    #         TextNode("This is text with a link ", TextType.TEXT),
    #         TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode(
    #             "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
    #         ),
    #     ]
    #     self.assertEqual(new_nodes, ans) 
    # def test_image(self):
    #     node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     TextType.TEXT,
    # )
    #     new_nodes = split_nodes_image([node])
    #     self.assertListEqual(
    #     [
    #         TextNode("This is text with an ", TextType.TEXT),
    #         TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    #         TextNode(" and another ", TextType.TEXT),
    #         TextNode(
    #             "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
    #         ),
    #     ],
    #     new_nodes,
    # )
    def test_full(self):
        s = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        myans = text_to_textnodes(s)
        ans = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(ans, myans)
if __name__ == "__main__":
    main()