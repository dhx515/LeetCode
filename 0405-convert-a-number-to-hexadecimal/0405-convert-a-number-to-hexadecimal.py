class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        # 16진수 변환에 사용할 문자들
        hex_chars = "0123456789abcdef"
        result = ""
        
        # 32비트로 변환 (음수 처리)
        num &= 0xFFFFFFFF
        
        while num > 0:
            digit = num % 16
            result += hex_chars[digit]
            num = num // 16
        
        # 결과 뒤집어서 반환
        return result[::-1]