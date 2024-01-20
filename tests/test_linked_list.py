"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    def setUp(self):
        self.A = Node({'num': 'num'})
        self.B = Node({"num": ("one", "five")})

    def test_init(self):
        self.assertEqual(self.A.data, {'num': 'num'})
        self.assertEqual(self.A.next_node, None)
        self.assertEqual(self.B.data, {"num": ("one", "five")})
        self.assertEqual(self.B.next_node, None)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.A = LinkedList()

    def test_init(self):
        self.assertEqual(self.A.tail, None)
        self.assertEqual(self.A.head, None)

    def test_insert_beginning(self):
        self.A.insert_beginning({'num': 'num'})
        self.assertEqual(str(self.A), "{'num': 'num'} -> None")
        self.A.insert_beginning({"num": ("one", "five")})
        self.assertEqual(str(self.A), "{'num': ('one', 'five')} -> {'num': 'num'} -> None")
        # with self.assertRaises(AttributeError):
        #     fault = self.A.tail.next_node.data

    def test_insert_at_end(self):
        self.A.insert_at_end({'num': 'num'})
        self.assertEqual(str(self.A), "{'num': 'num'} -> None")
        self.A.insert_at_end({"num": ("one", "five")})
        self.assertEqual(str(self.A), "{'num': 'num'} -> {'num': ('one', 'five')} -> None")

    def test_str(self):
        self.assertEqual(str(self.A), "None")

        self.A.insert_beginning({"num": ("one", "five")})
        self.A.insert_beginning({'num': 'num'})
        self.A.insert_at_end({'num': 'num'})
        self.assertEqual(str(self.A), "{'num': 'num'} -> {'num': ('one', 'five')} -> {'num': 'num'} -> None")
