"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestNode(unittest.TestCase):
    def setUp(self):
        self.A = Node(6, None)
        self.B = Node(("one", "two"), "three")

    def test_init(self):
        self.assertEqual(self.A.data, 6)
        self.assertEqual(self.A.next_node, None)
        self.assertEqual(self.B.data, ("one", "two"))
        self.assertEqual(self.B.next_node, "three")


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.A = Queue()

    def test_init(self):
        self.assertEqual(self.A.tail, "")
        self.assertEqual(self.A.head, None)
        self.assertEqual(self.A.all, [])

    def test_enqueue(self):
        self.A.enqueue([1, 2, 3, 4])
        self.A.enqueue(2)
        self.A.enqueue("item")
        self.assertEqual(self.A.head.data, [1, 2, 3, 4])
        self.assertEqual(self.A.head.next_node.next_node.data, "item")
        self.assertEqual(self.A.tail.data, "item")
        self.assertEqual(self.A.tail.next_node, None)
        with self.assertRaises(AttributeError):
            fault = self.A.tail.next_node.data

    def test_dequeue(self):
        self.A.enqueue(2)
        self.A.enqueue([1, 2, 3])
        self.assertEqual(self.A.dequeue(), 2)
        self.assertEqual(self.A.dequeue(), [1, 2, 3])
        self.assertEqual(self.A.dequeue(), None)

    def test_str(self):
        self.assertEqual(str(self.A), "")
        self.A.enqueue("one")
        self.A.enqueue("2")
        self.A.enqueue("item")
        self.assertEqual(str(self.A), "one\n2\nitem")
        self.A.dequeue()
        self.assertEqual(str(self.A), "2\nitem")
