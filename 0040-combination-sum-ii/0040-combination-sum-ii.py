class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()  # 중복 조합 방지를 위해 정렬

        def backtrack(start, target, path):
            if target == 0:  # 목표 값 도달 시 결과 추가
                result.append(list(path))
                return
            if target < 0:  # 목표 값 초과 시 종료
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # 같은 depth에서 중복 숫자 스킵
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)  # 다음 숫자 선택 (현재 숫자는 재사용 불가)
                path.pop()  # 백트래킹
        
        backtrack(0, target, [])
        return result