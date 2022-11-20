from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 1)
        memo[0] = 0
        memo[1] = 0
        for i in range(2, len(memo)):
            memo[i ] = min(cost[i-1] + memo[i-1], cost[i-2] + memo[i-2])
            
        return memo[-1]