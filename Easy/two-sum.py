from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_dict: Dict[int, int] = dict()
        for i, num in enumerate(nums):
            if target - num in number_dict:
                return [number_dict[target - num], i]
            number_dict[num] = i
        return [-1, -1]
