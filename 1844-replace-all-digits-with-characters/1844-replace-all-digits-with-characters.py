class Solution:
    def replaceDigits(self, s: str) -> str:
        l=list(s)
        for i,j in enumerate(l):
            if j.isdigit():
                l[i]=chr(ord(l[i-1])+int(j))
        return ''.join(l)