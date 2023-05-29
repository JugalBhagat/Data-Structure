class HeapTree:
    def __init__(self):
        self.heap=[]

    def insert(self,value):
        self.heap.append(value)
        self.adjust_up(len(self.heap)-1)

    def adjust_up(self,index):
        parent_index=(index-1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            self.adjust_up(parent_index)

    def extract_max(self):
        if not self.heap:
            return None
        maxx=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self.shift_down(0)
        return maxx
    
    def shift_down(self,index):
        maxx_index=index
        right_index= 2 * index + 2
        left_index= 2 * index + 1

        if(len(self.heap) > left_index and self.heap[left_index] > self.heap[maxx_index]):
            maxx_index=left_index

        if(len(self.heap) > right_index and self.heap[right_index] > self.heap[maxx_index]):
            maxx_index=right_index

        if(maxx_index != index):
            self.heap[index],self.heap[maxx_index]=self.heap[maxx_index],self.heap[index]
            self.shift_down(maxx_index)




x=HeapTree()

x.insert(12)
x.insert(24)
x.insert(20)
x.insert(9)
x.insert(1)
x.insert(10)
x.insert(6)
x.insert(2)


print(x.heap)

print(x.extract_max())
print(x.heap)