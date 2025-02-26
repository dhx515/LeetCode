class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total = m * n  # 전체 요소 개수
        k = k % total  # k가 전체 개수를 넘어갈 경우 최적화

        # 1️⃣ 2D grid -> 1D list 변환
        flat = [grid[i][j] for i in range(m) for j in range(n)]

        # 2️⃣ k번 오른쪽으로 이동 (리스트 슬라이싱 사용)
        flat = flat[-k:] + flat[:-k]

        # 3️⃣ 1D list -> 2D grid 변환
        return [[flat[i * n + j] for j in range(n)] for i in range(m)]