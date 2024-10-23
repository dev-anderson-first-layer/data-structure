class Deque:
    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        if self.empty():
            return
        self.deque.pop(0)
        self.len -= 1

    def pop_back(self):
        if self.empty():
            return
        self.deque.pop(self.len - 1)
        self.len -= 1

    def front(self):
        if self.empty():
            return
        return self.deque[0]

    def back(self):
        if self.empty():
            return
        return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end=' ')

d = Deque()
print(d.empty())
d.push_front(10)
print(d.empty())
d.push_front(5)
d.push_back(20)
d.push_front(7)
d.push_back(40)
d.show()
print('\nfront {}'.format(d.front()))
print('back: {}'.format(d.back()))

d.pop_back()
d.show()
print('\n')
d.pop_front()
d.show()