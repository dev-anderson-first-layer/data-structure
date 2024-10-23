from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
d.append(3)
d.appendleft(4)

for i in d:
    print(i, end=' ')

print('\n')
d.pop()

for i in d:
    print(i, end=' ')


print('\n')
d.remove(4)

for i in d:
    print(i, end=' ')