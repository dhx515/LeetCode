class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        ones = s.count('1')  # 전체 1의 개수
        zeros = 0  # 왼쪽 부분 0의 개수

        # 문자열을 1부터 len(s) - 1까지 분할하며 점수 계산
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            
            max_score = max(max_score, zeros + ones)

        return max_score