class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        for index, word in enumerate(sentence.split()):
            if word.startswith(searchWord):  # 접두사인지 확인
                return index + 1  # 1-based index 반환
        return -1
