class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        counter = [0 for i in range(len(T))]
        stack = [0]
        
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                top = stack.pop()
                counter[top] = i - top
            stack.append(i)
        
        return counter