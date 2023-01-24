class Solution(object):
    import heapq
    def maxProduct(self, nums):
        nums = [-s for s in nums]
        heapq.heapify(nums)
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        return abs((a+1)*(b+1))    
        