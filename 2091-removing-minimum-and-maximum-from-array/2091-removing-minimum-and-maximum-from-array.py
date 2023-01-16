class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = 99999999
        maxi_pos = nums.index(max(nums))
        mini_pos = nums.index(min(nums))
        mini = min(len(nums)-mini_pos+maxi_pos+1,mini) 
        mini = min(mini_pos+len(nums)-maxi_pos+1,mini)
        mini = min(max(len(nums)-mini_pos,len(nums)-maxi_pos),mini)
        mini = min(max(mini_pos,maxi_pos)+1,mini)
        return mini