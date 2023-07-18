class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray  = [1]
        postfixArray = [1]
        res = []
        # Populate prefix array
        for i in range(len(nums)-1):
            prefixArray.append(prefixArray[-1]* nums[i])
        # Populate postfix array
        for i in range(1, len(nums)):
            postfixArray.append(postfixArray[-1]* nums[-i])
        # Reverse the postfix array
        postfixArray = postfixArray[::-1]
        for i in range(len(nums)):
            res.append(prefixArray[i]*postfixArray[i])     
        return res
        