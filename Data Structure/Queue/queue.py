""" Queue implementation using Python List """

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def enqueue(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[0]

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0) #pops the first element from the list
