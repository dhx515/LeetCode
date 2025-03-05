class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        soldiers = []
        
        # 각 행에서 군인의 개수와 행 번호를 저장
        for i, row in enumerate(mat):
            count = sum(row)  # 군인의 수 (1의 개수)
            soldiers.append((count, i))  # (군인 수, 행 번호)
        
        # **군인 수 기준 정렬**, 같은 경우 행 인덱스 기준으로 정렬
        soldiers.sort(key=lambda x: (x[0], x[1]))
        
        # k개의 행 번호만 반환
        return [soldiers[i][1] for i in range(k)]