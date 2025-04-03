class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0

        for num in arr:
            if num % 2 == 1:  # 홀수일 경우
                count += 1
                if count == 3:
                    return True
            else:
                count = 0  # 짝수면 초기화

        return False