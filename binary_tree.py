def inorder_walk(x):
    if x:
        inorder_walk(x.left)
        print(x.key)
        inorder_walk(x.right)


def search(x, key):
    if x is None or x.key == key:
        return x
    if x.key > key:
        search(x.left, key)
    else:
        search(x.right, key)


def tree_min(x):
    if x is None:
        return x
    if x.left:
        tree_min(x.left)
    return x


def tree_successor(x):
    if x.right:
        return tree_min(x.right)
    y = x.p
    while y is not None and y.right == x:
        x = y
        y = x.p
    return y


def tree_insert(x, val):
    # z = BinaryTree(val)
    while x:
        y = x
        if x.key > val:
            x = x.left
        else:
            x = x.right
    z = BinaryTree(val)
    if y is None:
        return z
    z.p = y
    if y.key > val:
        y.left = z
    else:
        y.right = z


def tree_delete(z):
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_successor(z)
    # если у z 2 ребенка, то y = следующий элемент сразу за z

    if y.left is None:
        x = y.right
    else:
        x = y.left
    # x - единственный ребенок y. два быть не может
    # если он не равен null, то родитель y теперь родитель x. Убрали y из этой цепочки родит. ссылок
    if x:
        x.p = y.p

    if y.p:
        # если y - левый ребенок отцовского узла, то теперь левый ребенок отцовского узла - x
        if y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    #else:
        # x - теперь корень дерева
        # z.root = x

    if y != z:
        z.key = y.key

    return y


class BinaryTree:
    def __init__(self, key=None):
        __slots__ = ('p','key','left','right', 'root')
        self.p = None
        self.key = key
        self.right = None
        self.left = None
