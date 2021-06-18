from typing import Dict, List


def get_consecutive_elements_length(num: int, numbers_dict: List[int]) -> int:
    if not num in numbers_dict:
        return 0
    if numbers_dict[num] != -1:
        return numbers_dict[num]
    numbers_dict[num] = 1 + get_consecutive_elements_length(num - 1, numbers_dict)
    return numbers_dict[num]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer: int = 0
        numbers_dict: Dict[int, int] = dict()
        for num in nums:
            numbers_dict[num] = -1
        for num in nums:
            answer = max(answer, get_consecutive_elements_length(num, numbers_dict))
        return answer
