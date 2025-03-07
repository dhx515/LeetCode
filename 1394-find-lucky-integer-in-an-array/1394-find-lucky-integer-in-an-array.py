class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = Counter(arr)  # 빈도수 계산
        lucky_numbers = [num for num, count in freq.items() if num == count]  # 행운의 숫자 리스트
        
        return max(lucky_numbers) if lucky_numbers else -1  # 가장 큰 값 반환
        