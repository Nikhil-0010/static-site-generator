import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode('p', 'abc',props={"style": "color:'green';"})
        res = node1.props_to_html()
        self.assertEndsWith(res, ';"')
        
    def test_props_to_html_2(self):
        node = HTMLNode('p', 'abc')
        res = node.props_to_html()
        self.assertEqual("",res)
    
    def test_to_html(self):
        node = HTMLNode('p','abc')
        self.assertRaises(NotImplementedError, node.to_html)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )