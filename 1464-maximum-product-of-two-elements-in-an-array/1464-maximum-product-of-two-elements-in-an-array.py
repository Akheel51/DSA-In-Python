import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        m=nums[-1]
        n=nums[-2]
        ans=(m-1)*(n-1)
        return ans
        