def transitionPoint(arr, n):
    #Code here
    if n==1:
        if arr[0]==0:
            return -1
        else:
            return 0
    for i in range(n):
        if arr[i]==1:
            return i
    return -1        


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends