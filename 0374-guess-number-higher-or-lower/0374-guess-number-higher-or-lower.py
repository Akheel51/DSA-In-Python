class Solution:
    def guessNumber(self, n: int) -> int:
        l, r= 1, n                         
        while r >= l:                       
            m = (l + r)//2                 
            query =  guess(m)                                       
            if query ==  1:
                l = m+1         
            elif query == -1:
                r = m         							    
            else:
                return m