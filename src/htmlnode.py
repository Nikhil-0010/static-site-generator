class HTMLNode:
    def __init__(self, tag:str = None, value:str = None, children: list[HTMLNode] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_str = ""
        for key,val in self.props.items():
            props_str = f'{props_str} {key}="{val}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode{self.tag, self.value, self.children, self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value:str=None, props:dict = None):
        super().__init__(tag, value, None ,props)
    
    def to_html(self)-> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode{self.tag, self.value, self.props}'

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children: list[HTMLNode], props: dict = None):
        super().__init__(tag,None ,children, props=props)
    
    def to_html(self)-> str:
        if self.tag is None:
            raise ValueError("tag missing")
        if self.children is None:
            raise ValueError("children missing")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        props_str = self.props_to_html() if hasattr(self, 'props_to_html') else ""
            
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"