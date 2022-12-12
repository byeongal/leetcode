from typing import List


class Solution:
    def find_next_job(self, last_ending_time: int, job_list: List[int]) -> int:
        next_idx = len(job_list)
        start = 0
        end = len(job_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if job_list[mid][0] >= last_ending_time:
                next_idx = mid
                end = mid - 1
            else:
                start = mid + 1
        return next_idx

    def find_max_profit(self, idx: int, job_list: List[int], memo: List[int]):
        if idx == len(job_list):
            return 0
        if memo[idx] != -1:
            return memo[idx]
        next_idx = self.find_next_job(job_list[idx][1], job_list)
        memo[idx] = max(
            self.find_max_profit(idx + 1, job_list, memo),
            job_list[idx][2] + self.find_max_profit(next_idx, job_list, memo),
        )
        return memo[idx]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_list = []
        for i in range(len(startTime)):
            job_list.append((startTime[i], endTime[i], profit[i]))
        job_list.sort()
        memo = [-1] * len(job_list)
        return self.find_max_profit(0, job_list, memo)
