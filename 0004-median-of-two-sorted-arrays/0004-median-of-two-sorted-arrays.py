class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        if n % 2 == 1: #합쳐진 배열의 원소 갯수가 홀수개일 땐 가운데 값 리턴 
            answer = nums[n // 2]
        else: # 합쳐진 배열의 원소 갯수가 짝수개일 땐 가운데 두 값의 평균값 리턴
            answer = (nums[n // 2 - 1] + nums[n // 2]) / 2.0
            
        return answer