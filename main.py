from node import Node


"""Etsii ja palauttaa puusta noden jonka arvo on key
Jos tällaista nodea ei löydy, palauttaa None
Toimii rekursiolla. Aloittaa annetusta nodesta (oletuksena puun juuri).
Jokaisen noden kohdalla vertaa noden arvoa haluttuun arvoon. Jos pienempi, kutsuu
search funktion oikealle lapsisolmulle, koska oikealta löytyvät kaikki suuremmat arvot.
Jos solmun arvo on liian suuri, kutsuu fuktion vasemmalle. Jos arvo on oikea tai lapsisolmua ei
enää ole, palauttaa noden mihin jäätiin. Jos haluttua arvoa ei ole puussa, palauttaa None"""
def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


# Lisää root-nodesta alkavaan puuhun noden annetulla arvolla
# Ei tee mitään, jos annettu arvo on jo puussa
# liikkuu puussa rekursiivisesti
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
# Tulostettavat arvot jäävät fuktion kutsupinoon kunnes on niiden vuoro
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


# Alustaa puun ilman minkäänlaista optimointia
# Käyttää vals-listan ensimmäistä arvoa puun juurena
def init_tree(vals):
    root = Node(vals[0])
    for val in vals:
        root = insert(root, val)
    return root


# Nopea ja itse keksitty tapa välttää tehokkuuden kannalta huonoin tilanne
# Käyttää puun juurena listan mediaania
# Näin estetään pahin mahdollinen tapaus missä puu on käytännössä linkitetty lista
def init_quick_balance(vals):
    vals.sort()
    root_val = vals[len(vals) // 2]
    root = Node(root_val)
    vals.shuffle()
    for val in vals:
        root = insert(root, val)
    return root


def main():
    vals = [14, 7, 5, 3, 17, 12, 9, 10, 23, 1, 11]
    root = init_tree(vals)


main()
