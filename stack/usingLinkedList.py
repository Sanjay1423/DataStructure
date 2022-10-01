class Node:
    def __init__(self, value):
        self.node = {
            'Value': value,
            'Next': None
        }


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return f'Stack {{ top: {self.top}, bottom: {self.bottom}, length: {self.length}}}'

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value).node
        if (self.length == 0):
            self.top = newNode
            self.bottom = newNode
            self.length += 1
        else:
            container = self.top
            self.top = newNode
            self.top['Next'] = container
            self.length += 1

    def pop(self):
        self.top = self.top['Next']
        self.length -= 1

        if self.length == 0:
            self.bottom = None


stack = Stack()
stack.push('google')
stack.push('udemy')
stack.push('discord')
print(stack.peek())
