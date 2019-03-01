tree =  [3,3,3,1,2,1,1,2,3,3,4]
First_Letter = tree[0]
Second_Letter = tree[0]
res = 0
Cur = 0
M = 1
for num in tree:
    if num == Second_Letter:
        res += 1
        Cur += 1
    elif num == First_Letter:
        res += 1
        Cur = 1
        First_Letter = Second_Letter
        Second_Letter = num
    else:
        res = Cur + 1
        Cur = 1
        First_Letter = Second_Letter
        Second_Letter = num
    M = max(M,res)
print(M)

