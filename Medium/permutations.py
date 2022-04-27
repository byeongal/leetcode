from typing import List


def solve(nums: List[int], visit: List[bool], output: List[int], answer: List[List[int]]) -> None:
    if len(output) == len(nums):
        answer.append(output[:])
    else:
        for i in range(len(nums)):
            if visit[i] == False:
                output.append(nums[i])
                visit[i] = True
                solve(nums, visit, output, answer)
                visit[i] = False
                output.pop()


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visit = [False] * len(nums)
        solve(nums, visit, [], answer)
        return answer
