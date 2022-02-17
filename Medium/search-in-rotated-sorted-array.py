from typing import *


def find_pivot(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return right


def bsearch(nums: List[int], target: int, pivot_idx: int) -> int:
    left, right = 0, len(nums)
    while left <= right:
        mid = (left + right) // 2
        converted_mid = (mid + pivot_idx) % len(nums)
        if nums[converted_mid] == target:
            return converted_mid
        if nums[converted_mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot_idx = find_pivot(nums)
        return bsearch(nums, target, pivot_idx)