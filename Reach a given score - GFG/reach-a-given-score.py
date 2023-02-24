#User function Template for python3

def count(n):
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    for i in range(3,n+1):
        dp[i]+=dp[i-3]
    for i in range(5,n+1):
        dp[i]+=dp[i-5]
    for i in range(10,n+1):
        dp[i]+=dp[i-10]
    return dp[n]    
        
   
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends