from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left: int = max(weights)
        right: int = sum(weights)
        answer: int = right
        while left <= right:
            mid: int = (left + right) // 2
            needs: int = 1
            accumulated_weight: int = 0
            for weight in weights:
                if accumulated_weight + weight > mid:
                    needs += 1
                    accumulated_weight = 0
                accumulated_weight += weight
            if needs > days:
                left = mid + 1
            else:
                right = mid - 1
                answer = mid
        return answer
