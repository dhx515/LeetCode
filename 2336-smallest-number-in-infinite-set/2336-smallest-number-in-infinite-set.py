class SmallestInfiniteSet(object):

    def __init__(self):
        self.min_val = 1
        self.is_val_in_heap = {}
        self.heap = []

    def popSmallest(self):
        if not self.heap:
            smallest = self.min_val
            self.min_val +=1
        else:
            smallest = heappop(self.heap)
            del self.is_val_in_heap[smallest]
        
        return smallest

    def addBack(self, num):
        if num >= self.min_val or num in self.is_val_in_heap:
            return
        elif num == self.min_val - 1:
            self.min_val -= 1
        else:
            heappush(self.heap, num)
            self.is_val_in_heap[num] = True