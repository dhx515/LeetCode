class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0

        # Check if reshaping is possible
        if m * n != r * c or m == 0:
            return mat  # Return original matrix if not possible

        # Flatten the original matrix
        flat_list = [num for row in mat for num in row]

        # Build the reshaped matrix
        reshaped_mat = [flat_list[i * c:(i + 1) * c] for i in range(r)]

        return reshaped_mat