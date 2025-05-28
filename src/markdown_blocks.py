from enum import Enum

# from converter import text_node_to_html_node, text_to_textnodes
# from converter import text_node_to_html_node, text_to_textnodes
from converter import text_node_to_html_node, text_to_textnodes

from htmlnode import ParentNode
from textnode import TextNode, TextType    

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks  = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        html_node = block_to_html_node(block)
        # print(f"html_node: {html_node}\n")
        children.append(html_node)
    # print(len(children))
    parent_node = ParentNode("div",None, children, None)
    
    return parent_node

def paragraph_to_html(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",None, children, None)

def heading_to_html(block):
    i = 0
    while block[i] == "#":
        i += 1
    text = block[i+1:]
    if i + 1 >= len(block):
        raise ValueError(f"invalid heading level: {i}")
    children = text_to_children(text)
    return ParentNode(f"h{i}",None, children, None)

def code_to_html(block):
    # code blocks have a \n
    text = block[4:-3] 
    raw_text = TextNode(text,TextType.TEXT)
    child = text_node_to_html_node(raw_text)
    code = ParentNode("code", None, [child])
    # print(code.to_html())
    return ParentNode("pre", None, [code])

def quote_to_html(block : str):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    parent_node = ParentNode("blockquote",None,children)
    return parent_node

def unordered_list_to_html(block: str):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        li_parent_node = ParentNode("li", None, children)
        html_items.append(li_parent_node)
    ul_parent_node = ParentNode("ul",None, html_items)
    return ul_parent_node

def ordered_list_to_html(block: str):
    
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        li_parent_node = ParentNode("li",None, children)
        html_items.append(li_parent_node)
    ol_parent_node = ParentNode("ol",None,html_items)
    return ol_parent_node
    

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    # print(block_type)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if block_type == BlockType.HEADING:
        
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    if block_type == BlockType.ULIST:
        return unordered_list_to_html(block)
        
    if block_type == BlockType.OLIST:
       return ordered_list_to_html(block) 
    raise ValueError("invalid block type")

def block_to_block_type(block : str):
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH


    
