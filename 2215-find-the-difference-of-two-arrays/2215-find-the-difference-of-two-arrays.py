class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = [[],[]]
        nums3 = set(nums1)
        nums4 = set(nums2)
        answer[1] = nums4
        for i in nums3:
            if i not in nums4:
                answer[0].append(i)
            else:
                answer[1].remove(i)
        return answer