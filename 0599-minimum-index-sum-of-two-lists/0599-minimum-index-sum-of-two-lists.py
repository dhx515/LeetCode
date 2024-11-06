class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {string: idx for idx, string in enumerate(list1)}
        min_index_sum = float('inf')
        result = []
        
        for idx2, string in enumerate(list2):
            if string in index_map:
                index_sum = idx2 + index_map[string]
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    result = [string]
                elif index_sum == min_index_sum:
                    result.append(string)
        return result