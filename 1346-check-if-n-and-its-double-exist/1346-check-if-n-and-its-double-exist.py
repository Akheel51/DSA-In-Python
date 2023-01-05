class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums=set()
        for i in arr:
            if 2*i in nums or i/2 in nums:
                return True
            else:
                nums.add(i)
        return False            
       
