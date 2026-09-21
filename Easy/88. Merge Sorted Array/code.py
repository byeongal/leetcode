class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_point = m - 1
        nums2_point = n - 1
        cursor = m + n - 1
        while nums1_point >= 0 and nums2_point >= 0:
            if nums1[nums1_point] > nums2[nums2_point]:
                nums1[cursor] = nums1[nums1_point]
                nums1_point -= 1
            else:
                nums1[cursor] = nums2[nums2_point]
                nums2_point -= 1
            cursor -= 1
        while nums2_point >= 0:
            nums1[cursor] = nums2[nums2_point]
            nums2_point -= 1
            cursor -= 1
