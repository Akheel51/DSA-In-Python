class Solution:
    def hIndex(self, citations: List[int]) -> int:
        C = sorted(citations, reverse=True)
        for h in range(len(C)):
            if h+1>C[h]:
                return h
        return len(C)