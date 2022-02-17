from typing import *


def get_lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


def get_upper_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        lb = get_lower_bound(nums, target)
        ub = get_upper_bound(nums, target)
        if nums[lb] != target:
            return [-1, -1]
        return [lb, ub - 1]