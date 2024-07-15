class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0,0]
        for move in moves:
            if move == 'U':
                pos[1] -= 1
            elif move == 'D':
                pos[1] += 1
            elif move == 'L':
                pos[0] -= 1
            elif move == 'R':
                pos[0] += 1
        
        ans = False if pos != [0,0] else True
        return ans
            