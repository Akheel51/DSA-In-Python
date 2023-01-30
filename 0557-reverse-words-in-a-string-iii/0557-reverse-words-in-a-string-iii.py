class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        res=""
        for i in range(len(s)):
            if s[i]==" ":
                while len(stack)!=0:
                    res+=stack.pop()
                res+=" "    
            else:
                stack.append(s[i])
        if len(stack)==0:    
            return res
        else:
            while len(stack)!=0:
                res+=stack.pop()
        return res        
                
        
        