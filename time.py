import timeit


def time():
    setup_code = '''
from avl import AVLTree
from tree import Tree
import random

numberlist = random.sample(range(1, 10_000_000), 10000)

tree = Tree()
root_basic = tree.init_tree(numberlist)

tree_quick_bal = Tree()
root_quick_bal = tree_quick_bal.init_quick_balance(numberlist)

tree_avl = AVLTree()
root_avl = None
for val in numberlist:
    root_avl = tree_avl.insert_node(root_avl, val)
    '''

    test_code_basic = '''
num1 = tree.search(root_basic, numberlist[0]).key
num2 = tree.search(root_basic, numberlist[100]).key
num3 = tree.search(root_basic, numberlist[9999]).key
    '''

    test_code_quick_bal = '''
num1 = tree_quick_bal.search(root_quick_bal, numberlist[0]).key
num2 = tree_quick_bal.search(root_quick_bal, numberlist[100]).key
num3 = tree_quick_bal.search(root_quick_bal, numberlist[9999]).key
    '''

    test_code_avl = '''
num1 = tree_avl.search(root_avl, numberlist[0]).key
num2 = tree_avl.search(root_avl, numberlist[100]).key
num3 = tree_avl.search(root_avl, numberlist[9999]).key 
    '''

    time = timeit.timeit(setup=setup_code, stmt=test_code_basic, number=10000)
    print("Search time with basic tree: {}".format(time))

    time = timeit.timeit(setup=setup_code, stmt=test_code_quick_bal, number=10000)
    print("Search time with quicly balanced tree: {}".format(time))

    time = timeit.timeit(setup=setup_code, stmt=test_code_avl, number=10000)
    print("Search time with avl tree: {}".format(time))


if __name__ == "__main__":
    time()
