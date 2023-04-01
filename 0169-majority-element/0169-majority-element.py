class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        n=len(nums)
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i in hashmap:
            if hashmap[i]>n/2:
                return i
            