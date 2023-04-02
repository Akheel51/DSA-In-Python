class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        nums.sort()
        prev=nums[0]
        c,ans=1,1
        for i in range(1,n):
            if nums[i]==prev+1:
                c+=1
            elif nums[i]!=prev:
                c=1
            ans=max(ans,c)
            prev=nums[i]
        return ans    
                
            
        