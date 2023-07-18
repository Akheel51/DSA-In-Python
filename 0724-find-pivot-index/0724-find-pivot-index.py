class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        leftsum=0
        for i in range(n):
            rightsum=total-nums[i]-leftsum
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1    
        