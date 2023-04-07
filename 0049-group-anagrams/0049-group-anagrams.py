class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            sk = "".join(sorted(i))    
            if sk in d:
                d[sk].append(i)
            else:
                d[sk] = [i]
        return d.values()    