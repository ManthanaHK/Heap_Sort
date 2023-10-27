from maxHeap import *

heap = maxHeap([8,2,100,18,22,1030])
heap.addElement(20)
print(heap.testMaxHeap())
print(heap.data)
print("Extracted max element: ",heap.extractMaxEle())
print(heap.data)
print("Heap Property after extracting: ",heap.testMaxHeap())
print('Element Count: ',heap.getCount())
heap.heapSort()
print('Sorted Heap: ',heap.data)