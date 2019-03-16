class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        memo = {}
        def GamePlayer1(ChoseList,Current_Total,desiredTotal,memo):
            if not ChoseList:
                return False
            state = tuple(ChoseList)
            if state not in memo:
                memo[state] = False
                if max(ChoseList) + Current_Total >= desiredTotal:
                    memo[state] = True
                else:
                    for i in range(len(ChoseList)):
                        if not GamePlayer1(ChoseList[:i] + ChoseList[i+1:],Current_Total + ChoseList[i],desiredTotal,memo):
                            memo[state] = True
            return memo[state]

        if sum(range(maxChoosableInteger)) < desiredTotal:
            return False

        ChoseList = []
        for i in range(maxChoosableInteger):
            ChoseList.append(i+1)

        return GamePlayer1(ChoseList,0,desiredTotal,memo)
p = Solution()
print(sum(range(50)))
print(p.canIWin(5,50))
