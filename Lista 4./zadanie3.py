# Author: Patrycja Paradowska
# 10 kwietnia 2020r. Lista 4. Python, Zadanie 3.
# Napisac klase class Node(object) do reprezentacji pojedynczego wezla drzewa z dowolna liczba potomkow.
# Napisz funkcje, ktora generuje drzewo o danej wysokosci i generator, ktory przechodzi drzewo w porzadku DFS i BFS.

import random

class Node:
    def __init__(self, value, children, h):
        self.height = h
        self.value = value
        self.children = children

    def __str__(self):
        return f'{self.value} [{", ".join(str(s) for s in self.children)}]'

    def getNodeValue(self):
        return self.value


def random_tree(tree_size):
    if tree_size == 0:
        return None
    elif tree_size == 1:
        return Node(random.randint(-(tree_size ** 2), tree_size ** 2), [], 1)
    count = random.randint(1, 2)
    positionthehighest = random.randrange(0, count)
    v = random.randint(-tree_size ** 2, tree_size ** 2)
    tab_subtrees = []
    for i in range(count):
        if i != positionthehighest:
            _tree = random_tree(random.randint(1, tree_size - 1))
        else:
            _tree = random_tree(tree_size - 1)
        tab_subtrees.append(_tree)
    return Node(v, tab_subtrees, tree_size)


def depth_first_search(t):
    yield t.getNodeValue()
    for children in t.children:
        yield from depth_first_search(children)

def breadth_first_search(t):
    q = [t]
    while len(q) > 0:
        curr = []
        for subtree in q:
            yield subtree.getNodeValue()
            for node in subtree.children:
                curr.append(node)
        q = curr.copy()

if __name__ == '__main__':
    t = random_tree(3)
    print(t)
    print(list(breadth_first_search(t)))
    print(list(depth_first_search(t)))