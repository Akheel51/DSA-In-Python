class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[0]*(n+1)
        dp[0]=nums[0]
        for i in range(0,n-1):
            if dp[i]==0:
                return False
            dp[i+1]=max(dp[i]-1,nums[i+1])
        return True    
        