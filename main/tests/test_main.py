import unittest

import main
from RBTree import *
import Node

tree1 = RBTree()


class Test_select(unittest.TestCase):
    def test_TB1(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(6)
        tree1.insert(3)
        self.assertEqual(tree1.os_select(tree1.root, 4), None)

    def test_TB2(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(2)
        self.assertEqual(tree1.os_select(tree1.root, 2), 5)

    def test_TB3(self):
        tree1.root = None
        tree1.insert(5)
        self.assertEqual(tree1.os_select(tree1.root, 1), 5)

    def test_TB5(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(8)
        self.assertEqual(tree1.os_select(tree1.root, 2), 8)


class Test_rank(unittest.TestCase):
    def test_TB1(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(2)
        self.assertEqual(tree1.os_rank(tree1, 5), 2)

    def test_TB2(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(10)
        self.assertEqual(tree1.os_rank(tree1, 5), 1)

    def test_TB3(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(10)
        tree1.insert(1)
        tree1.insert(8)
        self.assertEqual(tree1.os_rank(tree1, 10), 4)

    def test_TB5(self):
        tree1.root = None
        tree1.insert(5)
        tree1.insert(2)
        self.assertEqual(tree1.os_rank(tree1, 5), 2)