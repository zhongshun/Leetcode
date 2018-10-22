def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 1:
        return ['()']
    elif n == 0:
        return []
    else:
        Last = generateParenthesis(n-1)
        New = []
        for Parenthes in Last:
            for j in range(n+1):
                #if '(' + Parenthes[0:j] + ')' + Parenthes[j:]not in New:
                New.append('(' + Parenthes[0:j] + ')' + Parenthes[j:])
        return list(set(New))


print(generateParenthesis(3))
