class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==1:
            return nums
        res=[]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>n/3:
                res.append(i)
        return res        
                
        