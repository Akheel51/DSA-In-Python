class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                nums.sort()
                res = []
                for i in range(len(nums)-1):
                    l = i + 1
                    r = len(nums) - 1
                    while l < r:
                        if nums[i] + nums[l] + nums[r] == 0:
                            res.append((nums[i], nums[l], nums[r]))
                            l += 1
                            r -= 1
                        elif nums[i] + nums[l] + nums[r] > 0:
                            r -= 1
                        else:
                            l += 1
                return set(res)