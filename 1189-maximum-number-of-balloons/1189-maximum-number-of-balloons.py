class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # "balloon"의 각 문자 필요 개수
        required = Counter("balloon")
        # 입력된 text에서 문자 개수 카운트
        text_count = Counter(text)
        
        # 필요한 문자별로 몇 번 만들 수 있는지 계산
        return min(text_count[c] // required[c] for c in required)