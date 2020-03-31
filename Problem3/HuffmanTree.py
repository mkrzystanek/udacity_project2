class Node:
    def __init__(self, char = None, freq = None):
        self.character = char
        self.frequency = freq
        self.left = None
        self.right = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def __repr__(self):
        values = self.character, self.frequency
        return str(values)

    def __str__(self):
        return "[{}, {}]".format(self.character, self.frequency)


class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            print()
            print(node)
            print("left:")
            print(node.left)
            print("right:")
            print(node.right)
            self._print_tree(node.left)
            self._print_tree(node.right)

