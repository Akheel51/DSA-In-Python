class Solution:
    def isValid(self, s: str) -> bool:
        # order = {")":"(", "}":"{", "]":"[" }
        # stack = list()

        # for x in range(len(s)):
        #     if s[x] in order.keys():
        #         if len(stack) == 0:
        #             return False
        #         elif stack.pop() != order[s[x]]: 
        #             return False
        #     else:
        #         stack.append(s[x])
        # if len(stack):
        #     return False
        # return True
        while('()' in s or  '{}' in s or '[]' in s):
            s = s.replace('()' , '')
            s = s.replace('[]' , '')
            s = s.replace('{}' , '')
                        
        if s != '' :
            return False
        else :
            return True