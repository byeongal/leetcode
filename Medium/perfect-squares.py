from typing import List


def get_perfect_list(n) -> List[int]:
    ret = []
    i = 1
    while i * i <= n:
        ret.append(i * i)
        i += 1

    return ret


class Solution:
    def numSquares(self, n: int) -> int:
        perfect_list: List[int] = get_perfect_list(n)
        memo: List[int] = [ i for i in range(0, n + 1) ]
        for i in range(1, n + 1):
            for perfect in perfect_list:
                if i - perfect < 0:
                    break
                memo[i] = min(memo[i], memo[i - perfect] + 1)
        return memo[n]


