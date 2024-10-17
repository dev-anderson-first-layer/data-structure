class Stack:
    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if self.empty():
            return
        self.stack.pop(self.len_stack - 1)
        self.len_stack -= 1

    def top(self):
        if self.empty():
            return
        return self.stack[-1]

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def length(self):
        return self.len_stack


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


