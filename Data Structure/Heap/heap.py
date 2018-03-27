"""MaxHeap implementation using python"""


class MaxHeap(object):

	def __init__(self, maxSize=None):
		self.heap = [float("inf")] # heap starting from index 1
		self.HEAP_SIZE = maxSize

	def _swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def _heapIsFull(self):
		return (self.HEAP_SIZE != None and len(self.heap) >= self.HEAP_SIZE)

	def insert(self, item):
		if self._heapIsFull():
			"Heap is full..."
		else:
			self.heap.append(item)
			# adjust parent node item
			self._bubbleUp(len(self.heap)-1)

	def _bubbleUp(self, currentPosition):
		if currentPosition >= 2: # no need to do bubbleUp for 1 element
			index = currentPosition
			parrentIndex = index//2

			if parrentIndex >= 0 and self.heap[parrentIndex] < self.heap[index]:
				self._swap(parrentIndex, index)
				self._bubbleUp(parrentIndex)
			
	def peek(self):
		return self.heap[1] if len(self.heap) > 1 else False

	def pop(self):
		element = self.peek()
		if element:
			self._swap(1, len(self.heap) - 1)
			self.heap.pop()
			self._bubbleDown(1)
		return element

	def _bubbleDown(self, index):
		leftChildIndex = 2 * index
		rightChildIndex = 2 * index + 1
		largest = index
		if len(self.heap) > leftChildIndex and self.heap[largest] < self.heap[leftChildIndex]:
			largest = leftChildIndex
		if len(self.heap) > rightChildIndex and self.heap[largest] < self.heap[rightChildIndex]:
			largest = rightChildIndex
		if largest!=index:
			self._swap(index, largest)
			self._bubbleDown(largest)
