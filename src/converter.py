from typing import List, Tuple
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
    regex_string = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_string, text)
    return matches
    
def extract_markdown_links(text):
    regex_string = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_string, text)
    return matches

def seperate_text_and_link(text) -> tuple[str,str]:
    text_link = r"\[(.*?)\]"
    link_text = r"\((.*?)\)"
    text_value = re.findall(text_link, text)[0]
    link_value = re.findall(link_text, text)[0]
    return (text_value, link_value)
def printlist(thelist):
    for textNode in thelist:
        print(textNode)
        print("")
    
def split_nodes_link(old_nodes:List[TextNode]):
    regex_string = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    res = []

    for node in old_nodes:
        text = node.text
        # text_links_tuple = extract_markdown_links(text)
        matches = re.finditer(regex_string, text)


        spans = []
        for match in matches:
            start, end = match.span()
            spans.append((start, end))
        
            # need to extract out the text of the link and the value
            # text_value, link_value = seperate_text_and_link(text[start:end])
        if spans == []:
            res.append(node)
            continue
        starting = 0
        
        for span_start, span_end in spans:
            # check if starting matches
            if span_start != starting and 0 <= starting < len(text):
                normal_text_section = text[starting: span_start]
                res.append(TextNode(normal_text_section ,TextType.TEXT, None))
                # part of node _link
            linked_string = text[span_start:span_end]
            text_value, link_value = seperate_text_and_link(linked_string)
            link_text_node = TextNode(text_value, TextType.LINK,link_value)
            res.append(link_text_node)
            starting = span_end
        if starting != len(text):
            normal_text_section = text[starting: starting: len(text)]
            res.append(TextNode(normal_text_section ,TextType.TEXT, None))
    # print(f"res: {res}")
    # print("start link")
    # printlist(res) 
    # print("end link")
    return res 


            
        
def split_nodes_image(old_nodes:List[TextNode]):
    regex_string = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    res = []
    # print("start image")
    # printlist(old_nodes) 
    # print("end image")
    for node in old_nodes:
        text = node.text
        # text_links_tuple = extract_markdown_links(text)
        matches = re.finditer(regex_string, text)
        # print(f"matches: {list(matches)}")
        spans = []
        for match in matches:
            start, end = match.span()
            spans.append((start, end))
            # print(f"Here: {text[start:end]}")
            # need to extract out the text of the link and the value
            # text_value, link_value = seperate_text_and_link(text[start:end])
        
        if spans == []:
            res.append(node)
            continue
        starting = 0
        for span_start, span_end in spans:
            # check if starting matches
            if span_start != starting and 0 <= starting < len(text):
                normal_text_section = text[starting: span_start]
                res.append(TextNode(normal_text_section ,TextType.TEXT, None))
                # part of node _link
            linked_string = text[span_start:span_end]
            text_value, link_value = seperate_text_and_link(linked_string)
            link_text_node = TextNode(text_value, TextType.IMAGE, link_value)
            res.append(link_text_node)
            starting = span_end
        if starting != len(text):
            normal_text_section = text[starting: len(text)]
            res.append(TextNode(normal_text_section ,TextType.TEXT, None))

    return res

def text_to_textnodes(text):
    # old nodes delmited , TEXT TYPE
    delmiter_to_type = {
        "`" : TextType.CODE,
        "**": TextType.BOLD,
        "_" : TextType.ITALIC,
    }
    curr_nodes = [TextNode(text,TextType.TEXT)]
    for key, value in delmiter_to_type.items():
        curr_nodes = split_nodes_delimiter(curr_nodes,key,value)
        # print(f"text_type: {value}, curr_nodes: {curr_nodes}")
    curr_nodes = split_nodes_image(curr_nodes)
    # printlist(curr_nodes)
    curr_nodes = split_nodes_link(curr_nodes)
    return curr_nodes

def markdown_to_blocks(markdown):
    # res = []
    markdown = markdown.strip()
    splitted = markdown.split("\n\n")
    res = [string for string in splitted if string ]
    # printlist(res)
    # print(res)
    # print(f"length: {len(res)}")
    return res