class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ps=[0]*n
        pe=[0]*n
        res=[0]*n
        ps[0]=nums[0]
        pe[-1]=nums[-1]
        for i in range(1,n):
            ps[i]=nums[i]*ps[i-1]   
        for i in range(n-2,-1,-1):
            pe[i]=nums[i]*pe[i+1]
        res[0]=pe[1]
        res[n-1]=ps[n-2]
        for i in range(1,n-1):
            res[i]=ps[i-1]*pe[i+1]
        return res    
            
        