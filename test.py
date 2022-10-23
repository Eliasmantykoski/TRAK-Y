import unittest
import timeit
import random
from avl import AVLTree
from tree import Tree


numberlist = random.sample(range(1, 10_000_000), 1000)


class TestTrees(unittest.TestCase):
    def test_basic_tree(self):
        tree = Tree()
        root = tree.init_tree(numberlist)
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[100]).key
        num3 = tree.search(root, numberlist[200]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        self.assertEqual(
            num2, numberlist[100],
            "num2 should be {0} not {1}".format(numberlist[100], num2)
        )
        self.assertEqual(
            num3, numberlist[200],
            "num3 should be {0} not {1}".format(numberlist[200], num3)
        )

    def test_quick_optimized_tree(self):
        tree = Tree()
        root = tree.init_quick_balance(numberlist)
        #t0 = time.time()
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[100]).key
        num3 = tree.search(root, numberlist[200]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        self.assertEqual(
            num2, numberlist[100],
            "num2 should be {0} not {1}".format(numberlist[100], num2)
        )
        self.assertEqual(
            num3, numberlist[200],
            "num3 should be {0} not {1}".format(numberlist[200], num3)
        )
        #t1 = time.time()
        #print("quick optimized tree used {}".format(t1-t0))

    def test_avl_tree(self):
        tree = AVLTree()
        root = None
        for val in numberlist:
            root = tree.insert_node(root, val)
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[100]).key
        num3 = tree.search(root, numberlist[200]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        self.assertEqual(
            num2, numberlist[100],
            "num2 should be {0} not {1}".format(numberlist[100], num2)
        )
        self.assertEqual(
            num3, numberlist[200],
            "num3 should be {0} not {1}".format(numberlist[200], num3)
        )
