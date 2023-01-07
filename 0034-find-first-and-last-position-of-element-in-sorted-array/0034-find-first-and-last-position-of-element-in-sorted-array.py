class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=nums[::-1]
        if target in nums:
            f=nums.index(target)
            l=len(ans)-ans.index(target)-1
            return [f,l]
        else:
            return [-1,-1]
        
        