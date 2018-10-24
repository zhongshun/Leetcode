def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n > 0:
        if not n%2:
            return myPow(x*x,n/2)
        else:
            return x*myPow(x*x,(n-1)/2)
    else:
        return myPow(1/x,-n)

x = 2
n = -2
print(myPow(x,n))
