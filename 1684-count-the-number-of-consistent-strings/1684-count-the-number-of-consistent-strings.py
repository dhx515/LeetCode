class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)  # allowed 문자열을 집합으로 변환
        count = 0
        
        # 각 단어를 검사
        for word in words:
            if all(char in allowed_set for char in word):  # 단어의 모든 문자가 allowed에 포함되는지 확인
                count += 1
                
        return count