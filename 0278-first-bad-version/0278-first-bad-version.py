# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # 불량 버전이므로 왼쪽 범위로 이동
            else:
                left = mid + 1  # 정상 버전이므로 오른쪽 범위로 이동

        return left  # left == right 이며, 첫 번째 불량 버전