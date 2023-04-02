class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                t1=target-(nums[i]+nums[j])
                l=j+1
                r=n-1
                while r>l:
                    if(nums[l]+nums[r]==t1):
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                        r-=1
                        l+=1
                    elif nums[l]+nums[r]>t1:
                        r-=1
                    else:
                        l+=1
        return ans