class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if not nums:
            return ans

        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                # 연속되는 숫자인 경우 끝점을 업데이트
                end = num
            else:
                # 연속되지 않는 경우 현재까지의 범위를 추가
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                # 새로운 범위 시작
                start = end = num

        # 마지막 범위를 추가
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))

        return ans