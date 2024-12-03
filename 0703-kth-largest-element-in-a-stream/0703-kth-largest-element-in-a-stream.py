class KthLargest(object):

    def __init__(self, k, nums):
        """
        Initialize the KthLargest object with integer k and initial stream nums.
        """
        self.k = k
        self.heap = []
        
        # Build the initial heap with at most k elements
        for num in nums:
            self.add(num)  # Reuse the add method to maintain heap property

    def add(self, val):
        """
        Add a new value to the stream and return the kth largest element.
        """
        # Add the new value to the heap
        heapq.heappush(self.heap, val)
        
        # If heap size exceeds k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # The root of the heap is the kth largest element
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)