class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # 우선순위 매핑 생성
        order_map = {char: index for index, char in enumerate(order)}
        
        # 두 단어 비교 함수
        def is_sorted(word1, word2):
            for c1, c2 in zip(word1, word2):
                if order_map[c1] < order_map[c2]:
                    return True
                elif order_map[c1] > order_map[c2]:
                    return False
            # 길이 비교: 짧은 단어가 앞에 와야 함
            return len(word1) <= len(word2)
        
        # 모든 인접한 단어 쌍을 비교
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        
        return True