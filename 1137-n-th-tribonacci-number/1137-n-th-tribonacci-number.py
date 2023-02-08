class Solution:
    def tribonacci(self, n: int) -> int:
        A = [0]*(n+1)
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        A[0] = 0
        A[1] = 1
        A[2] = 1
        for i in range(3, n+1):
            A[i] = A[i-1] + A[i-2] + A[i-3]
        return A[n]
        