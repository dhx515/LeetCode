class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        # chars의 문자 개수를 미리 저장
        char_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)  # 각 단어의 문자 개수 계산
            
            # 각 문자가 chars에서 충분히 제공되는지 확인
            if all(word_count[c] <= char_count[c] for c in word_count):
                total_length += len(word)  # 가능한 단어의 길이 합산
        
        return total_length