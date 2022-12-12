from typing import List


def find(matrix: List[List[int]], area: List[int], target: int) -> bool:
    left_up_y, left_up_x, right_down_y, right_down_x = area
    if left_up_y > right_down_y or left_up_x > right_down_x:
        return False
    mid_y = (left_up_y + right_down_y) // 2
    mid_x = (left_up_x + right_down_x) // 2
    if matrix[mid_y][mid_x] == target:
        return True
    if matrix[mid_y][mid_x] < target:
        return find(matrix, [mid_y + 1, left_up_x, right_down_y, right_down_x], target) or find(
            matrix, [left_up_y, mid_x + 1, right_down_y, right_down_x], target
        )
    else:
        return find(matrix, [left_up_y, left_up_x, right_down_y, mid_x - 1], target) or find(
            matrix, [left_up_y, left_up_x, mid_y - 1, right_down_x], target
        )


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return find(matrix, [0, 0, len(matrix) - 1, len(matrix[0]) - 1], target)
