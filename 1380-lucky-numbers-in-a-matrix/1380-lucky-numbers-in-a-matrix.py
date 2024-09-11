class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky_number = []
        for row in matrix:
            index, min_val = min(enumerate(row), key=itemgetter(1))
            if max([row[index] for row in matrix]) == min_val:
                lucky_number.append(min_val)

        return lucky_number