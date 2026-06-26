class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        dp0 = cost[0]
        dp1 = cost[1]
        for i in range(2, len(cost)):
            total = cost[i] + min(dp0,dp1)
            dp0 =  dp1
            dp1 = total
        return min(dp0,dp1)