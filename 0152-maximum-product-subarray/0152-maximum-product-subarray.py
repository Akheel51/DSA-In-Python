class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxp=float("-inf")
        prod=1
        for i in range(n):
            prod*=nums[i]
            maxp=max(maxp,prod)
            if prod==0:
                prod=1
        prod=1
        for i in range(n-1,-1,-1):
            prod*=nums[i]
            maxp=max(maxp,prod)
            if prod==0:
                prod=1
        return maxp        
                