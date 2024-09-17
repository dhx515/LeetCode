class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s = sorted(s)  # 문자열을 정렬
        while s:
            # 작은 문자부터 차례로 추가
            smallest = []
            for char in sorted(set(s)):  # 중복을 제거하고, 정렬된 상태에서 작은 것부터
                result.append(char)
                s.remove(char)  # 선택한 문자를 삭제

            # 큰 문자부터 차례로 추가
            largest = []
            for char in sorted(set(s), reverse=True):  # 큰 문자부터 작은 문자로
                result.append(char)
                s.remove(char)  # 선택한 문자를 삭제

        return ''.join(result)