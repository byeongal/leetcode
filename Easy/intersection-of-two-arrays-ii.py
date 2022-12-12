from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        answer = []
        for num in nums1:
            m[num] = m.get(num, 0) + 1
        for num in nums2:
            if m.get(num, 0) >= 1:
                answer.append(num)
                m[num] -= 1
        return answer
