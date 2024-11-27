import heapq


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))

    def remove(self):
        return heapq.heappop(self._queue)[-1]

queue = PriorityQueue()
queue.insert(Person('Maria'), 20)
queue.insert(Person('Pedro'), 16)
queue.insert(Person('Felipe'), 25)
queue.insert(Person('Carol'), 23)

print(queue.remove())