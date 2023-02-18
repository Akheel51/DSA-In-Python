class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                currSubset = subsets[i]
                subsets.append(currSubset + [num])
        return subsets