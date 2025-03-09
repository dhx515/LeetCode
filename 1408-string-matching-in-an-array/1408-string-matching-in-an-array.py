class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:  # 자기 자신은 비교하지 않음
                    result.add(words[i])  # 중복 방지를 위해 set 사용
        
        return list(result)