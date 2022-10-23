# Suuremmat arvot oikealle ja pienemmät vasemmalle.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1

