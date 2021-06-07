class Queue:

    def __init__(self):
        self.list = []

    def enque(self, ele):
        self.list.insert(0, ele)

    def deque(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list) - 1]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)


q = Queue()
print(q.isEmpty())
print(q.size())
q.enque(1)
print(q.size())
q.enque(2)
q.enque(3)
print(q.size())
print(q.deque())
print(q.size())
print(q.deque())
print(q.size())
