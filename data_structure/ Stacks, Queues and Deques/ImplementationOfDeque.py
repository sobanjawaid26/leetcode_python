class Deque:

    def __init__(self):
        self.list = []

    def addFront(self, ele):
        self.list.insert(0, ele)

    def addRear(self, ele):
        self.list.append(ele)

    def removeFront(self):
        return self.list.pop(0)

    def removeRear(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list)


d = Deque()
print('isEmpty == >', d.isEmpty())
d.addFront(2)
d.addRear(3)
d.addFront(1)
d.addRear(4)
print('isEmpty == >', d.isEmpty())
print('size == >', d.size())
print('removeRear 4 == >', d.removeRear())
print('removeFront 1 == >', d.removeFront())
print('removeFront 2 == >', d.removeFront())
