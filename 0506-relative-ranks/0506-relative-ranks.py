class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        # 점수와 원래 인덱스를 쌍으로 묶음
        score_with_index = [(s, i) for i, s in enumerate(score)]
        # 점수에 따라 내림차순 정렬
        score_with_index.sort(reverse=True)
        
        # 결과를 저장할 리스트 초기화
        ranks = [''] * n
        
        # 메달 이름 정의
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        # 순위 할당
        for rank, (s, idx) in enumerate(score_with_index):
            if rank < 3:
                ranks[idx] = medals[rank]
            else:
                ranks[idx] = str(rank + 1)
        
        return ranks