class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return  0

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(matrix)
B = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

n = len(matrix)
it_time =  int(n/2) + n%2
Rotated = []
L = []
for i in range(int(n/2)+n%2,n):
    matrix[i],matrix[-i-1] = matrix[-i-1],matrix[i]
print(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
