class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        n=len(words)
        c=0
        for i in range(n):
            if words[i]==s[:len(words[i])]:
                c+=1
        return c        
            
                
                
                