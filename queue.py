class Queue:
    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if self.empty():
            return
        self.queue.pop(0)
        self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if self.empty():
            return
        return self.queue[0]

queue = Queue()
print(queue.empty())
queue.push(1)
print(queue.empty())
queue.push(2)
print(queue.front())
queue.push(3)
print(queue.length())
queue.pop()
print(queue.front())
queue.pop()
print(queue.front())
queue.pop()
print(queue.front())
print(queue.length())
