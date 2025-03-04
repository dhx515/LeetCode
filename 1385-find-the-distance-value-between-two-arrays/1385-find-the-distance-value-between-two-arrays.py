class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()  # 이진 탐색을 위해 정렬
        count = 0
        
        for num in arr1:
            idx = bisect.bisect_left(arr2, num)  # num보다 크거나 같은 최소 위치 찾기
            # 현재 위치에서 거리 검사
            left_valid = (idx == 0 or abs(arr2[idx - 1] - num) > d)
            right_valid = (idx == len(arr2) or abs(arr2[idx] - num) > d)
            
            if left_valid and right_valid:
                count += 1
        
        return count