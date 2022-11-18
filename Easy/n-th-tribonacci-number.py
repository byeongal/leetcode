class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0] * max((n + 1), 3)
        T[0], T[1], T[2] = 0, 1, 1
        for i in range(3, n+1):
            T[i] = T[i-1] + T[i-2] + T[i-3]
        return T[n]