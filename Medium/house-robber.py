from typing import *

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [[0, 0] for _ in range(len(nums))]
        memo[0][0] = nums[0]
        memo[1][0] = nums[1]
        memo[1][1] = max(memo[0])
        for i in range(2, len(nums)):
            memo[i][0] = nums[i] + max(memo[i-2])
            memo[i][1] = max(memo[i-1])
        
        return max(memo[-1])