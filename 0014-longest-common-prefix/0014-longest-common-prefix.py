class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return " "
        s1,s2=min(strs),max(strs)
        i=0
        while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
            i+=1
        return s1[:i]