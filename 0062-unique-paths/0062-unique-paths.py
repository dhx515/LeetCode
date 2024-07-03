class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev=[0]*n  # 이전 행을 저장하는 리스트를 생성합니다.
        for i in range(m):
            temp=[0]*n  # 현재 행을 저장하는 리스트를 생성합니다.
            for j in range(n):
                if i==0 and j==0:
                    temp[j]=1  # 시작점(0, 0)은 경로의 수가 1입니다.
                    continue  # 다음 반복문으로 넘어갑니다.
                up=left=0
                if i>0:
                    up=prev[j]  # 위쪽 칸의 값을 가져옵니다.
                if j>0:
                    left=temp[j-1]  # 왼쪽 칸의 값을 가져옵니다.
                temp[j]=up+left  # 위쪽과 왼쪽에서 오는 경로의 수를 더합니다.
            prev=temp  # 현재 행을 이전 행으로 업데이트합니다.
        return prev[n-1]  # 마지막 칸의 값을 반환합니다.