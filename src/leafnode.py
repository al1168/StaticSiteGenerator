from htmlnode import HTMLNode
from typing import Optional, List, Dict
class LeafNode(HTMLNode): 
    def __init__(self, tag: Optional[str] = None, value: Optional[str]= None , children: Optional[List["HTMLNode"]] = None, props= None):
        if value == None:
            raise ValueError("Must have value")
        if children != None:
            raise ValueError("Leaf Node Must Not Have Children")
        super().__init__(tag, value, children, props)
    def to_html(self):
        if self.value  == None:
            raise ValueError("Leaf Node Must Have Value")
        if self.tag == None:
            return str(self.value)
        
        elif self.props:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        else: 
            return f'<{self.tag}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'