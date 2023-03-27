class Solution:
    def kItemsWithMaximumSum(self, Ones: int, Zeros: int,NegOnes: int, k: int) -> int:
        if Ones>=k:
            return k
        else:
            if Ones+ Zeros>=k: 
                return Ones
            else:
                diff = k-(Ones+Zeros) 
                return Ones-diff