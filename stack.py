class Stack:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if self.empty():
            return
        self.stack.pop(len(self.stack) - 1)

    def top(self):
        if self.empty():
            return
        return self.stack[-1]

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def length(self):
        return len(self.stack)


stack = Stack()
print(stack.empty())
print(stack.length())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.length())
print(stack.top())
print(stack.empty())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())


