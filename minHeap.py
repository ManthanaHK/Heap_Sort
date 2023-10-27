class maxHeap:
    def __init__(self,lst=[]):
        self.data = lst
        self._buildHeap_()
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def getCount(self):
        return len(self.data)
    
    def _parent_(self,idx):
        return (idx-1)//2
    
    def _lchild_(self,idx):
        return (2*idx + 1)
    
    def _rchild_(self,idx):
        return  (2*idx + 2)
    
    def _swap_(self,i,j):
        self.data[i],self.data[j] = self.data[j],self.data[i]
    
    def _buildHeap_(self):
        length = len(self.data)
        start = (length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap_(idx,length)
    
    def _downHeap_(self,idx,length):
        if self._lchild_(idx) < length:
            left = self._lchild_(idx)
            bigChild = left
            if self._rchild_(idx) < length:
                right = self._rchild_(idx)
                if self.data[right] < self.data[left]:
                    bigChild = right
            if self.data[bigChild] < self.data[idx]:
                self._swap_(bigChild,idx)
                self._downHeap_(bigChild,length)
    
    def addElement(self,element):
        self.data.append(element)
        self._upHeap_(len(self.data)-1)
    
    def _upHeap_(self,j):
        parent = self._parent_(j)
        if j>0 and self.data[j] < self.data[parent]:
            self._swap_(j,parent)
            self._upHeap_(parent)
    
    def testMinHeap(self):
        if not self.isEmpty():
            flag = 0
            for idx in range(len(self.data)-1,0,-1):
                if self.data[idx] > self.data[self._parent_(idx)]:
                    continue
                else:
                    flag = 1
        return flag != 1
    
    def heapSort(self):
        if not self.isEmpty():
            for idx in range(len(self.data)-1,0,-1):
                self._swap_(0,idx)
                self._downHeap_(0,idx)
    
    def getMinEle(self):
        if not self.isEmpty():
            return min(self.data)
        return None
    
    def extractMinEle(self):
        if not self.isEmpty():
            if len(self.data)==1:
                return self.data.pop()
            minimum = self.data.pop(0)
            self._downHeap_(0,len(self.data))
            return minimum

