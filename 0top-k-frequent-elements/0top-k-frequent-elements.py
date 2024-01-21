class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mem = {}
        for iter in nums:
            if iter not in mem.keys():
                mem[iter] = 1
            else:
                mem[iter] += 1
        
        tmp = []
        for key in mem.keys():
            tmp.append([mem[key], key])
        tmp.sort(reverse=True)
        
        res = []
        for iter in range(k):
            res.append(tmp[iter][1])
        
        return res