import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", "italic", "https://www.google.com")
        printed_node = "TextNode(This is a text node, italic, https://www.google.com)"
        self.assertEqual(str(node), printed_node)


if __name__ == "__main__":
    unittest.main()
