class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        elem = self.stack.pop()
        return elem

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
