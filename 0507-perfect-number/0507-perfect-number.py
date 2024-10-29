class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False  # 1 이하의 수는 완전수가 아님

        total = 1  # 1은 모든 수의 약수이므로 미리 더해줌
        import math
        sqrt_num = int(math.sqrt(num))

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                total += i
                divisor = num // i
                if divisor != i:
                    total += divisor
        return total == num