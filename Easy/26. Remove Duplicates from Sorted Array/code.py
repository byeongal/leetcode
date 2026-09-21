class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        right = 0
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1
        return left + 1
