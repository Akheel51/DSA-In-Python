class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1,p2=0,0
        n=len(s)
        m=len(t)
        while p1!=n and p2!=m:
            if s[p1]==t[p2]:
                p1+=1
            p2+=1
        if p1==n:
            return True
        return False
                
        