class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        
        result = []
        # 짝수와 홀수를 교대로 추가
        for even, odd in zip(evens, odds):
            result.append(even)  # 짝수 추가
            result.append(odd)   # 홀수 추가
        
        return result