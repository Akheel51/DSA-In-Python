class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1 and isBadVersion(n):
            return 1
        l = 1
        r = n

        while l <= r:
            mid = l + (r-l) // 2
            if isBadVersion(mid):
                if isBadVersion(mid -1) == False:
                    return mid
                else:
                    r = mid-1
            else:
                l = mid + 1 
            
        return 0
