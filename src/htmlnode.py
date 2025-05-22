from typing import Optional, List, Dict
class HTMLNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str]= None , children: Optional[List["HTMLNode"]] = None, props: Optional[Dict[str,str]]= None):
        self.tag = tag
        self.value = value  
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f'tag: {self.tag} value:{self.value} children:{self.children} props:{self.props}'
    
    def to_html(self):
       raise NotImplementedError
    
    def props_to_html(self) -> str:
        if isinstance(self.props, dict):
            attributes = [f'{key}="{value}"' for key,value in self.props.items()]
            return " ".join(attributes)
        return ""

class ParentNode(HTMLNode):
    def __init__(self, tag: Optional[str] = None, value: Optional[str]= None , children: Optional[List["HTMLNode"]] = None, props: Optional[Dict[str,str]]= None):
        if value:
            raise ValueError("Parent Node should not have a value")
        if not tag:
            raise ValueError("Tag should have a value")
        if not children:
            raise ValueError("Tag should have a value")
        super().__init__(tag,value,children,props)
    def to_html(self):
        if not self.tag:
            raise ValueError("Must have tag in Parent Node")
        if not self.children: 
            raise ValueError("Must have children in Parent Node")
        inner = []

        for child in self.children:
            inner.append(child.to_html())
        inner_string = "".join(inner) 
        if self.props:
            return f'<{self.tag} {self.props_to_html()}>{inner_string}</{self.tag}>'
        else:
            return f'<{self.tag}>{inner_string}</{self.tag}>'
