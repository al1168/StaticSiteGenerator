from enum import Enum

class TextType(Enum):
    NORMAL= "normal_text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text: str, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, otherTextNode:object) -> bool:
        if isinstance(otherTextNode, TextNode):
            return (otherTextNode.text == self.text and otherTextNode.text_type == self.text_type and self.url == otherTextNode.url) 
        return False
    def __repr__(self) ->str:
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    

    # Normal text
    # **Bold text**
    # _Italic text_
    # `Code text`
    # Links, in this format: [anchor text](url)
    # Images, in this format: ![alt text](url)
