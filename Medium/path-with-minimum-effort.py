import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])
        pq = []
        heapq.heappush(pq, (0, 0, 0))
        answer = 0
        seen = set()
        while pq:
            cost, y, x = heapq.heappop(pq)
            seen.add((y, x))
            print(cost, y, x)
            answer = max(cost, answer)
            if y == rows - 1 and x == columns - 1:
                break
            for ny, nx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                if not (0 <= ny < rows) or not (0 <= nx < columns):
                    continue
                if (ny, nx) in seen:
                    continue
                heapq.heappush(pq, (abs(heights[ny][nx] - heights[y][x]), ny, nx))
        return answer
