from minHeap import *

heap = maxHeap([80,34,56,0])
print(heap.data)
heap.addElement(-30)
print(heap.testMinHeap())
print(heap.getMinEle())
print(heap.extractMinEle())
print(heap.testMinHeap())
heap.heapSort()
print(heap.data)