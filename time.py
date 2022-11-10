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
import random
tree.search(root_basic, numberlist[random.randint(0, 9999)])
    '''

    test_code_quick_bal = '''
tree_quick_bal.search(root_quick_bal, numberlist[random.randint(0, 9999)])
    '''

    test_code_avl = '''
tree_avl.search(root_avl, numberlist[random.randint(0, 9999)])
    '''
    basic_times = []
    quick_times = []
    avl_times = []
    for i in range(10):
        time = timeit.timeit(setup=setup_code, stmt=test_code_basic, number=10000)
        print("Search time with basic tree: {}".format(time))
        basic_times.append(time)

        time = timeit.timeit(setup=setup_code, stmt=test_code_quick_bal, number=10000)
        print("Search time with quicly balanced tree: {}".format(time))
        quick_times.append(time)

        time = timeit.timeit(setup=setup_code, stmt=test_code_avl, number=10000)
        print("Search time with avl tree: {}\n".format(time))
        avl_times.append(time)
    basic_avg = sum(basic_times) / len(basic_times)
    quick_avg = sum(quick_times) / len(quick_times)
    avl_avg = sum(avl_times) / len(avl_times)
    return [basic_avg, quick_avg, avl_avg]


if __name__ == "__main__":
    avgs = time()
    print("Average search time with basic tree: {}".format(avgs[0]))
    print("Average search time with quicly balanced tree: {}".format(avgs[1]))
    print("Average search time with avl tree: {}".format(avgs[2]))
