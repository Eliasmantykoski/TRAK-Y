from node import Node


# Etsii ja palauttaa puusta noden jonka arvo on key
# Jos tällaista nodea ei löydy, palauttaa None
def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


# Lisää root-nodesta alkavaan puuhun noden annetulla arvolla
# Ei tee mitään, jos annettu arvo on jo puussa
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# Tulostaa puun arvot järjestyksessä
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Alustaa puun
# Käyttää vals-listan ensimmäistä arvoa puun juurena
def init_tree(vals):
    root = Node(vals[0])
    for val in vals:
        root = insert(root, val)
    return root


# Nopea ja helppo tapa välttää tehokkuuden kannalta huonoin tilanne
# Käyttää puun juurena listan mediaania
def init_quick_balance(vals):
    vals.sort()
    root_val = vals[len(vals) // 2]
    root = Node(root_val)
    vals.shuffle()
    for val in vals:
        root = insert(root, val)
    return root

#def init_avl(vals):



def main():
    vals = [14, 7, 5, 3, 17, 12, 9, 10, 23, 1, 11]
    root = init_tree(vals)

main()
