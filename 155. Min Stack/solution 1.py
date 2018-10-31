# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = self.getMin()
        if m == None or x < m:
            m = x
        self.p = self.p + [[x,m]]


    def pop(self):
        """
        :rtype: void
        """
        self.p.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.p[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.p:
            return None
        else:
            return self.p[-1][1]


obj = MinStack()
print(obj)
obj.push(0)
obj.push(1)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
