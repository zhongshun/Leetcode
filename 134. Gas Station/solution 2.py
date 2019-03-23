class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        Total_Tank = 0
        Current_Tank = 0
        start = 0
        for i in range(len(gas)):
            Total_Tank += gas[i] - cost[i]
            Current_Tank += gas[i] - cost[i]

            if Current_Tank < 0:
                start = i + 1
                Currnet_Tank = 0

        if Total_Tank < 0:
            return -1
        else:
            return start
p = Solution()
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(p.canCompleteCircuit(gas,cost))