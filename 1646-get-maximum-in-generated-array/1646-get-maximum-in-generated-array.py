class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        arr = [0]*(n+1)
        arr[1] = 1
        max_num = 0
        for i in range(2, n+1):
            if i%2 == 0:
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[i//2 + 1]
            max_num = max(max_num, arr[i])
        return max_num