class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 문자열이 팰린드롬인지 확인
        if s == s[::-1]:
            return 1
        # 팰린드롬이 아니면 두 번의 제거가 필요
        return 2