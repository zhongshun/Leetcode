class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def FindinRow(row, target):
            i = 0
            j = len(row) - 1
            while i <= j:
                if row[i] < target and row[j] > target:
                    i += 1
                    j -= 1
                elif row[i] == target or row[j] == target:
                    return True
                else:
                    return False
            return False

        if not matrix:
            return False

        for i in range(len(matrix) - 1):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                return FindinRow(matrix[i], target)
        return FindinRow(matrix[len(matrix) - 1], target)

p = Solution()
print(p.searchMatrix([[1],[3]],3))