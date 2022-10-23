from node import Node
from avl import AVLTree
import random





class Tree:
    # Alustaa puun ilman minkäänlaista optimointia
    # Käyttää vals-listan ensimmäistä arvoa puun juurena
    def init_tree(self, vals):
        root = Node(vals[0])
        for val in vals:
            root = self.insert(root, val)
        return root


    # Nopea ja itse keksitty tapa välttää tehokkuuden kannalta huonoin tilanne
    # Käyttää puun juurena listan mediaania
    # Näin estetään pahin mahdollinen tapaus missä puu on käytännössä linkitetty lista
    def init_quick_balance(self, vals):
        vals.sort()
        root_val = vals[len(vals) // 2]
        root = Node(root_val)
        random.shuffle(vals)
        for val in vals:
            root = self.insert(root, val)
        return root


    """Etsii ja palauttaa puusta noden jonka arvo on key
    Jos tällaista nodea ei löydy, palauttaa None
    Toimii rekursiolla. Aloittaa annetusta nodesta (oletuksena puun juuri).
    Jokaisen noden kohdalla vertaa noden arvoa haluttuun arvoon. Jos pienempi, kutsuu
    search funktion oikealle lapsisolmulle, koska oikealta löytyvät kaikki suuremmat arvot.
    Jos solmun arvo on liian suuri, kutsuu fuktion vasemmalle. Jos arvo on oikea tai lapsisolmua ei
    enää ole, palauttaa noden mihin jäätiin. Jos haluttua arvoa ei ole puussa, palauttaa None"""


    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)


    # Lisää root-nodesta alkavaan puuhun noden annetulla arvolla
    # Ei tee mitään, jos annettu arvo on jo puussa
    # liikkuu puussa rekursiivisesti
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.key == key:
                return root
            elif root.key < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root


    # Tulostaa puun arvot järjestyksessä
    # Tulostettavat arvot jäävät fuktion kutsupinoon kunnes on niiden vuoro
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)


"""def main():
    vals = [33, 13, 52, 9, 21, 61, 8, 11]
    tree = Tree()
    root = tree.init_tree(vals)
    avltree = AVLTree()
    root = None
    for val in vals:
        root = tree.insert(root, val)
    tree.inorder(root)
    print(tree.search(root, 9).key)
    #tree.printHelper(root, "", True)"""



