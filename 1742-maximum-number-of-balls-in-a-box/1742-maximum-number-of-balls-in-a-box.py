"""
당신은 공장에 근무하고 있으며, 여기서 번호가 lowLimit부터 highLimit까지인 총 n개의 공이 있습니다 (즉, n == highLimit - lowLimit + 1). 
그리고 1번부터 무한대까지 번호가 매겨진 상자들이 있습니다.

이 공장에서 당신의 일은 각 공을 공 번호의 각 자릿수의 합과 동일한 번호의 상자에 넣는 것입니다. 
예를 들어, 공 번호가 321이면 3 + 2 + 1 = 6이므로, 6번 상자에 공을 넣습니다. 공 번호가 10이면 1 + 0 = 1이므로 1번 상자에 공을 넣습니다.

두 정수 lowLimit과 highLimit이 주어졌을 때, 가장 많은 공이 들어 있는 상자의 공 개수를 반환하세요.
"""

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        from collections import defaultdict
        box_counts = defaultdict(int)

        for num in range(lowLimit, highLimit + 1):
            transformed = sum(int(i) for i in str(num))
            box_counts[transformed] += 1
        
        return max(box_counts.values())