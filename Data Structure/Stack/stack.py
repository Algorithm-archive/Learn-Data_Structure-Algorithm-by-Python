""" Stack implementation using Python List """

class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
