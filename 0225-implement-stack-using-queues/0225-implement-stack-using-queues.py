from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
            
        # 마지막 요소를 제거하여 반환
        res = self.queue1.popleft()
        
        # queue1과 queue2를 교환
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return res

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
            
        # 마지막 요소를 가져옴
        res = self.queue1.popleft()
        
        # 가져온 요소를 queue2에 추가
        self.queue2.append(res)
        
        # queue1과 queue2를 교환
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return 1 if not self.queue1 else 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()