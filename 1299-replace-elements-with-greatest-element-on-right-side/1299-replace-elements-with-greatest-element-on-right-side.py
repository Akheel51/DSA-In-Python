class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rightmax=-1
        for i in range(n-1,-1,-1):
            newmax=max(rightmax,arr[i])
            arr[i]=rightmax
            rightmax=newmax
        return arr    
            
            
        