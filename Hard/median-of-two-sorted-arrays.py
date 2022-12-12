from typing import List


def get_answer(nums1: List[int], nums2: List[int], nums1_idx: int, nums2_idx: int) -> float:
    total = 0
    iter = 2 if (len(nums1) + len(nums2)) % 2 == 0 else 1
    for i in range(iter):
        if nums1_idx == len(nums1):
            total += nums2[nums2_idx]
            nums2_idx += 1
        elif nums2_idx == len(nums2):
            total += nums1[nums1_idx]
            nums1_idx += 1
        elif nums1[nums1_idx] < nums2[nums2_idx]:
            total += nums1[nums1_idx]
            nums1_idx += 1
        else:
            total += nums2[nums2_idx]
            nums2_idx += 1
    return total / iter


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length == 1 or total_length == 2:
            return get_answer(nums1, nums2, 0, 0)
        median_idx = total_length // 2
        if total_length % 2 == 0:
            median_idx -= 1
        nums1_idx = nums2_idx = 0
        left_cnt = 0
        while nums1_idx < len(nums1) and nums2_idx < len(nums2):
            if nums1[nums1_idx] < nums2[nums2_idx]:
                nums1_idx += 1
            else:
                nums2_idx += 1
            left_cnt += 1
            if left_cnt == median_idx:
                return get_answer(nums1, nums2, nums1_idx, nums2_idx)
        while nums1_idx < len(nums1):
            nums1_idx += 1
            left_cnt += 1
            if left_cnt == median_idx:
                return get_answer(nums1, nums2, nums1_idx, nums2_idx)
        while nums2_idx < len(nums2):
            nums2_idx += 1
            left_cnt += 1
            if left_cnt == median_idx:
                return get_answer(nums1, nums2, nums1_idx, nums2_idx)
        return 0.0
