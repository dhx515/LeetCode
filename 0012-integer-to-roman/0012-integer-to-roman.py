class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mem = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'
        }
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        res = ''
        tmp = num
        while tmp > 0:
            for iter in value:
                if iter <= tmp:
                    res += mem[iter]
                    tmp -= iter
                    break
        return res