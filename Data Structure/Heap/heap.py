"""MaxHeap implementation using python"""


class MaxHeap(object):

	HEAP_SIZE = 10

	def __init__(self):
		self.heap = [0]*MaxHeap.HEAP_SIZE
		self.currentPosition = -1

	def _swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def _heapIsFull(self):
		if self.currentPosition == MaxHeap.HEAP_SIZE:
			return True
		return False

	def insert(self, item):
		if self._heapIsFull():
			"Heap is full..."
			return
		self.currentPosition+=1
		self.heap[self.currentPosition] = item
		# adjust parent node item
		self._bubbleUp(self.currentPosition)

	def _bubbleUp(self, currentPosition):
		index = currentPosition
		parrentIndex = index//2

		if parrentIndex>=0 and self.heap[parrentIndex] < self.heap[index]:
			self._swap(parrentIndex, index)
			# index = parrentIndex
			self._bubbleUp(parrentIndex)
			

	def getMax(self):
		if self.heap[0]:
			return self.heap[0]
		else:
			return "Empty Heap"

	def pop(self):
		if self.currentPosition > 1:
			# swap first element with last element
			self._swap(0,self.currentPosition)
			del self.heap[self.currentPosition]
			# adjust parent node item
			self._bubbleDown(0)
		elif self.currentPosition == 1:
			del self.heap[0]
		else:
			print "No deletion operation for empty heap"
			return "False"

	def _bubbleDown(self, index):
		left = 2*index+1
		right = 2*index+2
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest!=index:
			self._swap(index, largest)
			self._bubbleDown(largest)

	def printHeap(self):
		all_hp_element = []
		for i in self.heap:
			if i!=0:
				all_hp_element.append(i)
		return all_hp_element

			