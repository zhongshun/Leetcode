class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = len(matrix)

        while i < j:
            if matrix[i][-1] < target:
                i += 1
            if matrix[j][0] > target:
                j -= 1
        if target in matrix[i] or target in matrix[j]:
            return True
        return False


p = Solution()
print(p.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))