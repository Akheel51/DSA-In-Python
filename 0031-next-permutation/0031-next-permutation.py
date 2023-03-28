class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = x = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0 :
            nums.reverse()
            return
        while nums[x] <= nums[i - 1]:
            x -= 1
        nums[i - 1], nums[x] = nums[x], nums[i - 1]
        nums[i:] = nums[len(nums) - 1: i - 1: - 1]
        return nums
            
        
        