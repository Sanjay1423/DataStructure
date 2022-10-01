
class Node:
    def __init__(self, value):
        self.node = {
            "value": value,
            "next": None
        }


class linkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return f'LinkedList {{ head: {self.head}, tail: {self.tail}, length: {self.length} }}'

    def printList(self):
        array = []
        currentNode = self.head
        while currentNode != None:
            array.append(currentNode['value'])
            currentNode = currentNode['next']
        return array

    def append(self, value):
        newNode = Node(value).node
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return f'LinkedList {{ head: {self.head}, tail: {self.tail}, length: {self.length} }}'

    def prepend(self, value):
        newNode = Node(value).node
        newNode['next'] = self.head
        self.head = newNode
        self.length += 1
        return f'LinkedList {{ head: {self.head}, tail: {self.tail}, length: {self.length} }}'

    def traversal(self, index):
        currentNode = self.head
        counter = 0
        while counter != index:
            currentNode = currentNode['next']
            counter += 1

        return currentNode

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
            return self.printList()
        elif index <= 0:
            self.prepend(value)
            return self.printList()
        else:
            leaderNode = self.traversal(index-1)
            holdNode = leaderNode['next']
            newNode = Node(value).node
            leaderNode['next'] = newNode
            newNode['next'] = holdNode
            self.length += 1
            return self.printList()

    def delete(self, index):
        if index < 0 or self.length < index:
            return "Index out of range"

        elif index == 0:
            self.head = self.head['next']
            return self.printList()
        else:
            leaderNode = self.traversal(index-1)
            chainNode = leaderNode['next']['next']
            leaderNode['next'] = chainNode
            self.length -= 1
            return self.printList()


link1 = linkedList(0)
link1.append(10)
link1.append(20)
link1.append(30)
link1.append(40)
link1.append(50)
print(link1.delete(1))
