import unittest
import random
from avl import AVLTree
from tree import Tree


numberlist = random.sample(range(1, 1000), 15)

# Testit kolmen eri puun hakufunktioon
# Puut alustetaan viidellätoista satunnaisella numerolla ja niistä haetaan kolmea numeroa jokaisesta
class TestTrees(unittest.TestCase):
    def test_basic_tree(self):
        print("\nTesting basic binary tree")
        tree = Tree()
        root = tree.init_tree(numberlist)
        print("Tree initialized with 15 random numbers")
        tree.inorder(root)
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[10]).key
        num3 = tree.search(root, numberlist[14]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        print("\nSearch for {} found {}".format(numberlist[0], num1))
        self.assertEqual(
            num2, numberlist[10],
            "num2 should be {0} not {1}".format(numberlist[5], num2)
        )
        print("\nSearch for {} found {}".format(numberlist[5], num2))
        self.assertEqual(
            num3, numberlist[14],
            "num3 should be {0} not {1}".format(numberlist[14], num3)
        )
        print("\nSearch for {} found {}".format(numberlist[14], num3))

    def test_quick_optimized_tree(self):
        print("\nTesting quickly optimized tree")
        tree = Tree()
        root = tree.init_quick_balance(numberlist)
        print("Tree initialized with 15 random numbers")
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[5]).key
        num3 = tree.search(root, numberlist[14]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        print("\nSearch for {} found {}".format(numberlist[0], num1))
        self.assertEqual(
            num2, numberlist[5],
            "num2 should be {0} not {1}".format(numberlist[5], num2)
        )
        print("\nSearch for {} found {}".format(numberlist[5], num2))
        self.assertEqual(
            num3, numberlist[14],
            "num3 should be {0} not {1}".format(numberlist[14], num3)
        )
        print("\nSearch for {} found {}".format(numberlist[14], num3))

    def test_avl_tree(self):
        print("\nTesting AVl tree")
        tree = AVLTree()
        root = None
        for val in numberlist:
            root = tree.insert_node(root, val)
        print("Tree initialized with 15 values")
        num1 = tree.search(root, numberlist[0]).key
        num2 = tree.search(root, numberlist[5]).key
        num3 = tree.search(root, numberlist[14]).key
        self.assertEqual(
            num1, numberlist[0],
            "num1 should be {0} not {1}".format(numberlist[0], num1)
        )
        print("\nSearch for {} found {}".format(numberlist[0], num1))
        self.assertEqual(
            num2, numberlist[5],
            "num2 should be {0} not {1}".format(numberlist[5], num2)
        )
        print("\nSearch for {} found {}".format(numberlist[5], num2))
        self.assertEqual(
            num3, numberlist[14],
            "num3 should be {0} not {1}".format(numberlist[14], num3)
        )
        print("\nSearch for {} found {}".format(numberlist[14], num3))
