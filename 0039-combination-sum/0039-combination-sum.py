class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(remaining, start, path):
            if remaining == 0:  # 목표 값 달성
                result.append(list(path))
                return
            elif remaining < 0:  # 목표 초과 시 백트래킹
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])  # 숫자 선택
                backtrack(remaining - candidates[i], i, path)  # 같은 숫자를 다시 사용할 수 있음
                path.pop()  # 백트래킹
        
        backtrack(target, 0, [])
        return result