from typing import List
from htmlnode import HTMLNode
from textnode import TextNode, TextType
import re
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
def split_nodes_delimiter(old_nodes: List[TextNode], delimiter, text_type)->List[TextNode]:
    res = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            res.append(old_node)
            continue
        split_nodes = [] # stores the nodes we split
        sections = old_node.text.split(delimiter)
        for i in range(len(sections)):
            value = sections[i] 
            if value == "":
                continue
            if i % 2 == 0:
                # create text
                split_nodes.append(TextNode(value, TextType.TEXT))
            else:  
                split_nodes.append(TextNode(value, text_type))
        res.extend(split_nodes)
    return res
def extract_markdown_images(text):
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    ""
    regex_string = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_string, text)
    return matches
    
def extract_markdown_links(text):
    regex_string = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_string, text)
    return matches

def split_nodes_link(node:List[TextNode]):
    pass
    # extract_markdown_links()
        
