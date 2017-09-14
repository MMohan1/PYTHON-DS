class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class LinkList():
    def __init__(self, data, node):
        self.head = None

    def isEmpty(self):
        return self.head == 0

    def addElement(self, data):
        node = Node(data)
        node.setData(data)
        node.setNext(self.head)
        self.head = node

    def getSize(self):
        current = self.head
        count = 0
        if not current:
            while current:
                count += 1
                current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        found = False
        pervious = None
        while current:
            if current.getData() == item:
                found = True
            else:
                pervious = current
                current = current.getNext()

        if not pervious:
            self.head = current.getNext()
        else:
            pervious.setNext(current.getNext())
