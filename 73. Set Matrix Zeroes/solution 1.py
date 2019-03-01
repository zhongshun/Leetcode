matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
x= []
y = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            x.append(i)
            y.append(j)
print(x,y)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in x or j in y:
            matrix[i][j] = 0
print(matrix)
