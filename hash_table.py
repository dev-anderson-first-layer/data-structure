import sys

class HashTable:
    def __init__(self, table_size):
        if table_size < 1:
            print('The size of table needs can be more than zero')
            sys.exit(1)

        self.table_size = table_size
        self.table = [[] for i in range(table_size)]

    def hash_func(self, key):
        return key % self.table_size

    def insert(self, key):
        self.table[self.hash_func(key)].append(key)

    def show(self):
        for linked_list in self.table:
            if not linked_list:
                continue
            for key in linked_list:
                print('{}'.format(key), end=' ')
            print('')

    def search(self, key):
        if key in self.table[self.hash_func(key)]:
            return True
        return False

hash_table = HashTable(9)

hash_table.insert(19)
hash_table.insert(28)
hash_table.insert(20)
hash_table.insert(5)
hash_table.insert(33)
hash_table.insert(15)

hash_table.show()
print(hash_table.search(19))
print(hash_table.search(50))
