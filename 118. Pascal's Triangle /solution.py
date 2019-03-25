class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        res = [[1]]
        for i in range(1,numRows):
            new = []
            new.append(1)
            for j in range(1,i):
                new.append(res[i-1][j-1] + res[i-1][j])
            new.append(1)
            res.append(new)
        return res