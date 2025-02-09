class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 32비트 정수 범위 처리
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        # 예외 처리: 나누는 수가 1 또는 -1일 때
        if divisor == 1:
            return min(max(dividend, INT_MIN), INT_MAX)
        if divisor == -1:
            return min(max(-dividend, INT_MIN), INT_MAX)

        # 부호 결정
        negative = (dividend < 0) ^ (divisor < 0)  # XOR 연산으로 부호 결정
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        # 비트 시프트를 활용한 나눗셈 (O(logN))
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # divisor * 2^k를 찾는다.
                temp <<= 1  # divisor를 2배씩 증가
                multiple <<= 1  # 몫도 2배씩 증가

            # 뺄셈 진행
            dividend -= temp
            quotient += multiple

        # 부호 적용
        if negative:
            quotient = -quotient

        # 정수 범위 제한
        return min(max(quotient, INT_MIN), INT_MAX)