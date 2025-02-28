class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        count = 1  # 현재 숫자의 개수 저장
        
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                count += 1
            else:
                count = 1  # 새로운 숫자가 나오면 count 초기화

            if count > n / 4:  # 25% 초과 확인
                return arr[i-1]

        return arr[0]  # 길이가 1이면 arr[0] 리턴