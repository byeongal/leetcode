from queue import PriorityQueue
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [False] * n
        visit = [False] * n
        memo[0] = True
        pq = PriorityQueue()
        pq.put(-0)
        while not pq.empty():
            cur = pq.get()
            if visit[cur]:
                continue
            visit[cur] = True
            if cur == n:
                return True
            for i in range(0, nums[cur]):
                next_idx = i + cur
                if next_idx > n:
                    break
                if memo[next_idx]:
                    continue
                memo[next_idx] = True
                pq.put(next_idx)
        return False
