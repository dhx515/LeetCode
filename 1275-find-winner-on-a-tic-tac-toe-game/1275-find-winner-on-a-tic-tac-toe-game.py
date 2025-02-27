class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        board = [[" "] * 3 for _ in range(3)]  # 3x3 빈 그리드 생성

        # moves를 순회하면서 배치
        for i, (r, c) in enumerate(moves):
            board[r][c] = "X" if i % 2 == 0 else "O"

        # 승리 여부 체크 함수
        def check_winner(player):
            # 가로, 세로 체크
            for i in range(3):
                if all(board[i][j] == player for j in range(3)): return True  # 가로
                if all(board[j][i] == player for j in range(3)): return True  # 세로

            # 대각선 체크
            if all(board[i][i] == player for i in range(3)): return True  # 좌상단 → 우하단
            if all(board[i][2-i] == player for i in range(3)): return True  # 우상단 → 좌하단

            return False

        # A가 이겼는지 확인
        if check_winner("X"):
            return "A"
        # B가 이겼는지 확인
        elif check_winner("O"):
            return "B"
        # 모든 칸이 찼다면 무승부
        elif len(moves) == 9:
            return "Draw"
        # 게임이 아직 진행 중이라면 "Pending"
        else:
            return "Pending"