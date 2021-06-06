class Stack:
    def __init__(self):
        self.list = []

    def push(self, ele):
        self.list.append(ele)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[len(self.list) - 1]

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)


s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
s.push(3)
print(s.size())
print(s.pop())
print(s.pop())
print(s.size())
print(s.isEmpty())