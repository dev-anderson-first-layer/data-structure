class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index < 0:
            return

        node = Node(label)

        if self.empty():
            self.first = node
            self.last = node
            self.len_list += 1
            return

        if index == 0:
            node.set_next(self.first)
            self.first = node
            self.len_list += 1
            return

        if index >= self.len_list:
            self.last.set_next(node)
            self.last = node
            self.len_list += 1
            return

        prev_node = self.first
        curr_node = self.first.get_next()
        curr_index = 1

        while not curr_node is None:
            if curr_index == index:
                node.set_next(curr_node)
                prev_node.set_next(node)
                break
            prev_node = curr_node
            curr_node = curr_node.get_next()
            curr_index += 1

        self.len_list += 1


    def pop(self, index):
        if self.empty() and index < 0 and index > self.len_list:
            return

        if self.first.get_next() is None:
            self.first = None
            self.last = None
            self.len_list -= 1
            return

        if index == 0:
            self.first = self.first.get_next()
            self.len_list -= 1
            return

        flag_remove = False
        prev_node = self.first
        curr_node = self.first.get_next()
        curr_index = 1
        while not curr_node is None:
            if index == curr_index:
                prev_node.set_next(curr_node.get_next())
                curr_node.set_next(None)
                flag_remove = True
                break

            prev_node = curr_node
            curr_node = curr_node.get_next()
            curr_index += 1

        if flag_remove:
            self.len_list -= 1

    def empty(self):
        if self.first is None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):
        curr_node = self.first

        while not curr_node is None:
            print(curr_node.get_label(), end=' ')
            curr_node = curr_node.get_next()
        print('')


linked_list = LinkedList()
linked_list.push('Marcos', 0)
linked_list.show()
linked_list.push('Maria', 1)
linked_list.show()
linked_list.push('Yankee', 0)
linked_list.show()
linked_list.push('Catarina', 2)
linked_list.show()
linked_list.push('Lilica', 4)
linked_list.show()
linked_list.push('Sara', 2)
linked_list.show()
print('Tamanho da lista {}\n'.format(linked_list.length()))

linked_list.pop(0)
linked_list.show()
linked_list.pop(2)
linked_list.show()
linked_list.pop(3)
linked_list.show()

print('Tamanho da lista {}\n'.format(linked_list.length()))
