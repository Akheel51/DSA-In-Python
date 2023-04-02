class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        numset=set(nums)
        for n in numset:
            if n-1 not in numset:
                curr=n
                c=1
                while curr+1 in numset:
                    curr+=1
                    c+=1
                count=max(count,c)
        return count    
                
            
        