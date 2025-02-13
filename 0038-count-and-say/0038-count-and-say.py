class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        result = "1"
        for _ in range(n - 1):
            next_sequence = ""
            count = 1  # 현재 문자 개수
            prev_char = result[0]  # 첫 번째 문자 저장
            
            for i in range(1, len(result)):
                if result[i] == prev_char:
                    count += 1  # 같은 문자 연속되면 증가
                else:
                    next_sequence += str(count) + prev_char  # 압축 문자열 생성
                    prev_char = result[i]  # 새로운 문자로 변경
                    count = 1  # 개수 초기화
            
            next_sequence += str(count) + prev_char  # 마지막 문자 처리
            result = next_sequence  # 다음 반복에서 사용할 문자열로 설정
        
        return result