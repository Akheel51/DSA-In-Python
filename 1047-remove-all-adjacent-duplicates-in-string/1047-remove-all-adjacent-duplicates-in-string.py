class Solution:
    def removeDuplicates(self, s: str) -> str:
        a,n=[],len(s)
        for i in range(n):
            if len(a)!=0 and a[-1]==s[i]:
                a.pop()
            else:
                a.append(s[i])
        return ''.join(a)