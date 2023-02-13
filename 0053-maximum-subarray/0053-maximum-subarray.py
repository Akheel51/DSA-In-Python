class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        m=nums[0]
        c=nums[0]
        start,end,s=0,0,0
        for i in range(1,n):
            if c<0:
                c=nums[i]
                s=i
            else:
                c+=nums[i]
            if m<c:
                m=c
                start=s
                end=i
        return m
        
        