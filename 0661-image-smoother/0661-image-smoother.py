class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(img), len(img[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt = 0
                tmp = 0
                for dx in range(-1, 2, 1):
                    if not 0 <= i+dx < m:
                        continue
                    for dy in range(-1, 2, 1):
                        if not 0 <= j+dy < n:
                            continue
                        cnt += 1
                        tmp += img[i+dx][j+dy]
                ans[i][j] = tmp//cnt
        return ans