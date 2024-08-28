class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            # result를 왼쪽으로 1 비트 이동
            result <<= 1
            # n의 마지막 비트를 result의 끝에 추가
            result |= (n & 1)
            # n을 오른쪽으로 1 비트 이동
            n >>= 1
        return result