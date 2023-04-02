class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        charset=set()
        ans,p=0,0
        for i in range(n):
            while s[i] in charset:
                charset.remove(s[p])
                p+=1
            charset.add(s[i])
            ans=max(ans,i-p+1)
        return ans    
        