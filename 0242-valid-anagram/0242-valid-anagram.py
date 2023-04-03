class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t=list(t)
        s=list(s)
        s.sort()
        t.sort()
        return s==t
        