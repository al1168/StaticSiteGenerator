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
