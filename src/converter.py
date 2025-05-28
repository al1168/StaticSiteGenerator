from typing import List, Tuple
from htmlnode import HTMLNode
from textnode import TextNode, TextType
import re
# from htmlnode import
from leafnode import LeafNode
from enum import Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST ="ordered_list"

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
        props = {"href" : text_node.url}
        return LeafNode("a",text_node.text,None, props)
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
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
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
            # print(text_value, link_value)
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
            # print(link_text_node.url)
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
    curr_nodes = split_nodes_link(curr_nodes)
    curr_nodes = split_nodes_image(curr_nodes)
    for key, value in delmiter_to_type.items():
        curr_nodes = split_nodes_delimiter(curr_nodes,key,value)
        # print(f"text_type: {value}, curr_nodes: {curr_nodes}")
    # printlist(curr_nodes)
    return curr_nodes

def markdown_to_blocks(markdown:str) -> List[str]:
    # res = []
    markdown = markdown.strip()
    splitted = markdown.split("\n\n")
    res = [string for string in splitted if string ]
    return res

def block_to_block_type(block_string: str):
    # check 
    if block_string == "":
        return BlockType.PARAGRAPH
    
#     Headings start with 1-6 # characters, followed by a space and then the heading text.
    if block_string[0] == "#":
        return BlockType.HEADING

    # Code blocks must start with 3 backticks and end with 3 backticks.
    if len(block_string) >= 6 and block_string[:3] == "```" and block_string[len(block_string)-3 : len(block_string)] == "```":
        return BlockType.CODE
    # Every line in a quote block must start with a > character.
    if block_string[0] == ">":
        return BlockType.QUOTE
    # Every line in an unordered list block must start with a - character, followed by a space.
    if len(block_string) >= 2 and block_string[:2] == "- ":
        return BlockType.UNORDERED_LIST
    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    if len(block_string) >= 2 and block_string[0].isnumeric() and block_string[1] == "." and block_string[2] == " ": 
        return BlockType.ORDERED_LIST
    # If none of the above conditions are met, the block is a normal paragraph.
    return BlockType.PARAGRAPH

def strip_heading_prefix(string : str):
    num_hash_tags = 0
    i = 0
    while i < len(string) and string[i] == '#':
        i += 1
        num_hash_tags  += 1
    return (num_hash_tags, string[i+1:])

def strip_code_prefix(string:str):
    return string[3:len(string)-3]

def create_nested_quote_nodes(string:str):
   pass 

    
def markdown_to_html_node(markdown):
    # any markdown 
    blocks = markdown_to_blocks(markdown)
    blockType_blocks_tuple = [(block, block_to_block_type(block)) for block in blocks]
    nodes = []
    if len(blockType_blocks_tuple) == 1 and blockType_blocks_tuple[0][1] == BlockType.PARAGRAPH:
        
        return 
    for block, block_type in blockType_blocks_tuple:
        if block_type == BlockType.PARAGRAPH:
            nodes.append(LeafNode("p", block, None, None))
        elif block_type == BlockType.HEADING:
            heading_size, adjusted_string = strip_heading_prefix(block)
            new_node = LeafNode(f'h{heading_size}',adjusted_string)
            nodes.append(new_node)
        elif block_type == BlockType.CODE:
            adjusted_string = strip_code_prefix(block)
            new_node = LeafNode("code",adjusted_string)
            nodes.append(new_node) 
        elif block_type == BlockType.QUOTE:
            # recurse
            pass