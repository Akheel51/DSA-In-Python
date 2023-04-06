class Solution:
    def lengthOfLastWord(self,s):
        S=list(map(str,s.split()))
        word=S[-1]
        return len(word)
        