# Author: Patrycja Paradowska
# 10 kwietnia 2020r. Lista 4. Python, Zadanie 2.
# Napisac funkcje, ktora generuje w sposob losowy drzewo o podanej
# wysokosci oraz przechodzi drzewo w porzadku DFS i BFS.

import random

def depth_first_search(t):
    if t is not None:
        yield t[0]
        yield from depth_first_search(t[1])
        yield from depth_first_search(t[2])

def breadth_first_search(t):
    q = [t]
    while len(q) > 0:
        curr = q.pop(0)
        if curr[1] is not None:
            q.append(curr[1])
        if curr[2] is not None:
            q.append(curr[2])
        yield curr[0]

def random_tree(tree_size):
    if tree_size == 0: # wysokosc
        return None

    v = random.randint(-(tree_size ** 2), tree_size ** 2)
    children = random_tree(random.randint(0, tree_size - 1))
    height_subtree = random_tree(tree_size - 1)

    if random.choice([True, False]):
        return [v, children, height_subtree]
    return [v, height_subtree, children]

if __name__ == '__main__':
    t = random_tree(3)
    print(t)
    print(list(depth_first_search(t)))
    print(list(breadth_first_search(t)))