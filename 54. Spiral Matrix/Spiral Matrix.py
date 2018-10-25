def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    m = len(matrix)
    s = matrix[0]
    n = len(s)
    point = -1
    x = 0
    y = n - 1
    count = n
    for step in range(max(len(matrix[0]),len(matrix)) - 1):
        if count == len(matrix)*len(matrix[0]):
            return s
        if point == -1:
            for j in range(m - 1):
                x = x + 1
                s = s + [matrix[x][y]]
                count = count + 1
            for i in range(n - 1):
                y = y - 1
                s = s + [matrix[x][y]]
                count = count + 1
            m = m - 1
            n = n - 1
            point = -point
        elif point == 1:
            for j in range(m - 1):
                x = x - 1
                s = s + [matrix[x][y]]
                count = count + 1
            for i in range(n - 1):
                y = y + 1
                s = s + [matrix[x][y]]
                count = count + 1
            m = m - 1
            n = n - 1
            point = -point
    return s





matrix = [
  [3],
  [2],
]


print(spiralOrder(matrix))
