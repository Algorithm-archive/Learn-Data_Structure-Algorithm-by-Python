from queue import Queue

queue = Queue()
queue.enqueue(10)
queue.enqueue(15)

print(queue.isEmpty())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.isEmpty())
