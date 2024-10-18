class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        if turnedOn < 0 or turnedOn > 10:
            return res  # 유효한 LED 개수가 아니면 빈 리스트 반환
        
        for h in range(12):  # 시간은 0부터 11까지
            for m in range(60):  # 분은 0부터 59까지
                # 켜져 있는 비트 수 계산
                total_bits = bin(h).count('1') + bin(m).count('1')
                if total_bits == turnedOn:
                    # 시간 형식에 맞게 문자열로 변환하여 추가
                    res.append("{}:{:02d}".format(h, m))
        return res