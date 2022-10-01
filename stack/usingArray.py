
class Stack:
    def __init__(self):
        self.array = []

    def __str__(self):
        return f'Stack {{{self.array}}}'

    def push(self, value):
        self.array.insert(0, value)

    def pop(self):
        self.array.pop(0)

    def peek(self):
        return self.array[0]


stack = Stack()
stack.push('google')
stack.push('udemy')
stack.push('discord')
stack.pop()
print(stack.peek())

print(stack)
