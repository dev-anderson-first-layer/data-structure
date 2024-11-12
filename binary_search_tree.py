class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        node = Node(label=label)

        if self.empty():
            self.root = node
            return

        dad_node = None
        curr_node = self.root

        while True:

            if curr_node is None:
                if node.get_label() < dad_node.get_label():
                    dad_node.set_left(node)
                else:
                    dad_node.set_right(node)
                break

            dad_node = curr_node
            if node.get_label() < curr_node.get_label():
                curr_node = curr_node.get_left()
            else:
                curr_node = curr_node.get_right()

    def remove(self, label):
        dad_node = None
        curr_node = self.root

        while not curr_node is None:
            if label == curr_node.get_label():
                if curr_node.get_left() is None and curr_node.get_right() is None:
                    if dad_node is None:
                        self.root = None
                    else:
                        if dad_node.get_left() == curr_node:
                            dad_node.set_left(None)
                        elif dad_node.get_right() == curr_node:
                            dad_node.set_right(None)
                elif (curr_node.get_left() is None and not curr_node.get_right() is None) or (
                        not curr_node.get_left() is None and curr_node.get_right() is None):
                    if dad_node is None:
                        if not curr_node.get_left() is None:
                            self.root = curr_node.get_left()
                        else:
                            self.root = curr_node.get_right()
                    else:
                        if not curr_node.get_left() is None:
                            if dad_node.get_left() and dad_node.get_left().get_label() == curr_node.get_label():
                                dad_node.set_left(curr_node.get_left())
                            else:
                                dad_node.set_right(curr_node.get_left())
                        else:
                            if dad_node.get_left() and dad_node.get_left().get_label() == curr_node.get_label():
                                dad_node.set_left(curr_node.get_right())
                            else:
                                dad_node.set_right(curr_node.get_right())
                elif not curr_node.get_left() is None and not curr_node.get_right() is None:
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.get_right()
                    next_smaller = curr_node.get_right().get_left()

                    while not next_smaller is None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.get_left()

                    if dad_node is None:
                        if self.root.get_right().get_label() == smaller_node.get_label():
                            smaller_node.set_left(self.root.get_left())
                        else:
                            if dad_smaller_node.get_left() and (
                                    dad_smaller_node.get_left().get_label() == smaller_node.get_label()):
                                dad_smaller_node.set_left(None)
                            else:
                                dad_smaller_node.set_right(None)

                            smaller_node.set_left(curr_node.get_left())
                            smaller_node.set_right(curr_node.get_right())
                        self.root = smaller_node
                    else:
                        if dad_node.get_left() and dad_node.get_left().get_label() == curr_node.get_label():
                            dad_node.set_left(smaller_node)
                        else:
                            dad_node.set_right(smaller_node)

                        if dad_smaller_node.get_left() and dad_smaller_node.get_left().get_label() == smaller_node.get_label():
                            dad_smaller_node.set_left(None)
                        else:
                            dad_smaller_node.set_right(None)

                        smaller_node.set_left(curr_node.get_left())
                        smaller_node.set_right(curr_node.get_right())
                break

            dad_node = curr_node
            if label < curr_node.get_label():
                curr_node = curr_node.get_left()
            else:
                curr_node = curr_node.get_right()

    def empty(self):
        if not self.root:
            return True
        return False

    def show(self, curr_node):
        if curr_node is None:
            return

        print('{}'.format(curr_node.get_label()), end=' ')
        self.show(curr_node=curr_node.get_left())
        self.show(curr_node=curr_node.get_right())

    def get_root(self):
        return self.root


binary_search_tree = BinarySearchTree()

binary_search_tree.insert(8)
binary_search_tree.insert(3)
binary_search_tree.insert(1)
binary_search_tree.insert(6)
binary_search_tree.insert(4)
binary_search_tree.insert(7)
binary_search_tree.insert(10)
binary_search_tree.insert(14)
binary_search_tree.insert(13)
binary_search_tree.insert(9)

binary_search_tree.remove(8)
binary_search_tree.show(binary_search_tree.get_root())