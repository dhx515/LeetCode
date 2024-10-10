class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        # 길이 확인
        if len(pattern) != len(words):
            return False
        
        # 매핑을 위한 딕셔너리 초기화
        char_to_word = {}
        word_to_char = {}
        
        # 패턴 문자와 단어를 동시에 순회
        for c, w in zip(pattern, words):
            # 문자 -> 단어 매핑 확인
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False  # 매핑 불일치
            else:
                char_to_word[c] = w  # 새로운 매핑 추가
            
            # 단어 -> 문자 매핑 확인
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False  # 매핑 불일치
            else:
                word_to_char[w] = c  # 새로운 매핑 추가
        
        # 모든 검증을 통과하면 True 반환
        return True