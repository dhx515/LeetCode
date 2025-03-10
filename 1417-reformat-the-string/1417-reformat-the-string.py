class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        digits = []

        # 문자와 숫자를 분리
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)

        # 번갈아 배치할 수 없는 경우 처리
        if abs(len(letters) - len(digits)) > 1:
            return ""

        # 문자 개수가 더 많으면 letters를 먼저, 아니면 digits를 먼저
        if len(letters) < len(digits):
            letters, digits = digits, letters  # swap

        # 결과 문자열 조합
        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])

        # 문자가 하나 더 많을 경우 마지막에 추가
        if len(letters) > len(digits):
            result.append(letters[-1])

        return "".join(result)