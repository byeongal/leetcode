class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1
        for i in range(pointer, len(nums)):
            nums[i] = None
        return pointer
