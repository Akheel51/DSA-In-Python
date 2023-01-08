class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = math.ceil((high-low)/2)
        if (high % 2 != 0 and low % 2 !=0):
            count+=1
        return count