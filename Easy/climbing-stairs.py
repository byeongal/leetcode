from typing import List

class Solution:
    def solve(self, n: int, memo:List[int])->int:
        if n < 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.solve(n-1, memo) + self.solve(n-2, memo)
        return memo[n]
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[1] = 1
        memo[0] = 1
        return self.solve(n, memo)
        