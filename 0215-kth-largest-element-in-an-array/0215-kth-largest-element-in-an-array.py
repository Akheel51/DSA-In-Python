class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
	    minhp = []
	    for i in nums:
		    heapq.heappush(minhp,i)
		    if len(minhp) > k:
			    heapq.heappop(minhp)
	    return minhp[0]  
        