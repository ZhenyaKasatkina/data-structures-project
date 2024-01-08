"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    def setUp(self):
        self.A = Node(data=5)
        self.B = Node(("one", "two"), "three")

    def test_init(self):
        self.assertEqual(self.A.data, 5)
        self.assertEqual(self.A.next_node, None)
        self.assertEqual(self.B.data, ("one", "two"))
        self.assertEqual(self.B.next_node, "three")


class TestStack(unittest.TestCase):
    def setUp(self):
        self.A = Stack()

    def test_init(self):
        self.assertEqual(self.A.top, None)

    def test_push(self):
        self.A.push([1, 2, 3, 4])
        self.A.push(2)
        self.A.push("item")
        self.assertEqual(self.A.top.data, "item")
        self.assertEqual(self.A.top.next_node.next_node.data, [1, 2, 3, 4])
        with self.assertRaises(AttributeError):
            fault = self.A.top.next_node.next_node.next_node.data

    def test_pop(self):
        self.A.push([1, 2, 3, 4])
        self.A.push("привет!")

        self.assertEqual(self.A.pop(), "привет!")
        self.assertEqual(self.A.pop(), ([1, 2, 3, 4]))
        self.assertEqual(self.A.top, None)

    def test_str(self):
        self.assertEqual(self.A.top, None)
        self.A.top = 2 + 3
        self.assertEqual(self.A.top, 5)
