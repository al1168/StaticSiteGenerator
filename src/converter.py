from textnode import TextNode, TextType
# from htmlnode import
from leafnode import LeafNode
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text,None,None)
    elif text_node.text_type == TextType.BOLD:
       return LeafNode("b",text_node.text,None,None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i",text_node.text,None,None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text,None,None)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text,None,None)
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img",text_node.text,None,None)
    else:
        raise NotImplementedError(f"Did not implement for {text_node}")
