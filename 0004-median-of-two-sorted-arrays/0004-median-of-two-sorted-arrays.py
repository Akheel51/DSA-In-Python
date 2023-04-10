class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        n=len(nums1)+len(nums2)
        nums3=nums1+nums2
        nums3.sort()
        if (n)%2==0:
            ans=(nums3[int(n/2)]+nums3[int(n/2-1)])/2
        else:
            ans=(nums3[int(n/2)])
        return ans
        
        