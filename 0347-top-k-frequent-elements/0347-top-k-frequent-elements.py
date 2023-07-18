class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        heap = []
        for i in freq_table.keys():
            if len(heap) == k:
                heappushpop(heap, (freq_table[i], i))
            else:
                heappush(heap, (freq_table[i], i))
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        return ans 