from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        number_dict = {}
        for num in nums:
            if num not in number_dict:
                number_dict[num] = 0
            number_dict[num] += 1
        unique_number_list = list(number_dict.keys())
        unique_number_list.sort()
        memo = [[0, 0] for _ in range(len(unique_number_list))]
        memo[0][0] = number_dict[unique_number_list[0]] * unique_number_list[0]
        if len(unique_number_list) == 0:
            return memo[0][0]
        for i in range(1, len(unique_number_list)):
            if unique_number_list[i] - unique_number_list[i-1] > 1:
                memo[i][0] = (number_dict[unique_number_list[i]] * unique_number_list[i]) + max(memo[i-1])
            else:
                memo[i][0] = (number_dict[unique_number_list[i]] * unique_number_list[i]) + memo[i-1][1]
            memo[i][1] = max(memo[i-1])
        return max(memo[-1])
        