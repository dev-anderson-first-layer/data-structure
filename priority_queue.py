class Person:
    def __init__(self, name, prior):
        self.name = name
        self.prior = prior

    def get_name(self):
        return self.name

    def get_prior(self):
        return self.prior


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.len = 0

    def push(self, person):
        if self.empty():
            self.pq.append(person)
            self.len += 1
            return

        flag_push = False
        for i in range(self.len):
            if not self.pq[i].get_prior() < person.get_prior():
                continue
            self.pq.insert(i, person)
            flag_push = True
            break

        if not flag_push:
            self.pq.insert(self.len, person)

        self.len += 1

    def pop(self):
        if self.empty():
            return
        self.pq.pop(0)
        self.len -= 1

    def empty(self):
        if self.len == 0:
            return True
        return False

    def show(self):
        for p in self.pq:
            print('Nome: {}'.format(p.get_name()))
            print('Prioridade: {}'.format(p.get_prior()))


p1 = Person('Marcos', 28)
p2 = Person('Catarina', 3)
p3 = Person('Pedro', 20)
p4 = Person('João', 35)

priority_queue = PriorityQueue()
priority_queue.push(p1)
priority_queue.push(p2)
priority_queue.push(p3)
priority_queue.push(p4)

priority_queue.show()

priority_queue.pop()
priority_queue.pop()

print()
priority_queue.show()

priority_queue.push(Person('Goku', 30))
print()
priority_queue.show()