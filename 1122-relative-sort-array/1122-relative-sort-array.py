class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # Step 1: 빈도수 저장
        count = Counter(arr1)
        result = []
        
        # Step 2: arr2의 순서 유지하며 삽입
        for num in arr2:
            result.extend([num] * count[num])  # 해당 숫자를 count[num]만큼 추가
            del count[num]  # 추가한 후 제거
        
        # Step 3: arr2에 없는 숫자들을 정렬 후 추가
        remaining = sorted(count.keys())  # 남은 숫자 정렬
        for num in remaining:
            result.extend([num] * count[num])  # 정렬된 순서대로 추가
        
        return result