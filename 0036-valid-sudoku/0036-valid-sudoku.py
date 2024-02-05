class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        mem1 = defaultdict(int)
        mem2 = [[defaultdict(int) for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue
                key_r = 'r'+str(r)+cur
                key_c = 'c'+str(c)+cur
                if key_r in mem1 or key_c in mem1:
                    return False
                    exit()
                elif cur in mem2[r//3][c//3].keys():
                    return False
                    exit()
                else:
                    mem1[key_r]
                    mem1[key_c]
                    mem2[r//3][c//3][cur]
        return True