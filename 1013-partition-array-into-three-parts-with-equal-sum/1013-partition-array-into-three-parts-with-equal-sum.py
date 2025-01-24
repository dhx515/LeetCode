class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, it's impossible to partition
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        current_sum = 0
        parts = 0
        
        for num in arr:
            current_sum += num
            
            # Check if we found a valid part
            if current_sum == target:
                parts += 1
                current_sum = 0
                
                # If we found 3 parts, return True
                if parts == 3:
                    return True
        
        # If we finish the loop and don't find exactly 3 parts, return False
        return False