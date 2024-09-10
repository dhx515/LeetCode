class Solution(object):
    def freqAlphabets(self, s):
        # 1-9는 'a'에서 'i', 10#-26#는 'j'에서 'z'로 매핑
        mapping = {str(i): chr(96 + i) for i in range(1, 27)}  # 1 -> 'a', 26 -> 'z'
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                # 뒤에서 세 번째 문자까지 숫자를 파싱해 변환
                result.append(mapping[s[i-2:i]])
                i -= 3  # '#', 숫자 두 개를 한 번에 처리
            else:
                # 한 자리 숫자를 변환
                result.append(mapping[s[i]])
                i -= 1

        return ''.join(result[::-1]) 