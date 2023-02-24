#User function Template for python3
class Solution:
    def countBT (self, h):
        if h==0 or h==1:
            return 1
        mod=int(1e9+7)
        dp=[0]*(h+1)
        dp[0],dp[1]=1,1
        for i in range(2,h+1):
            dp[i]=(dp[i-1] * (2*dp[i-2] +dp[i-1])) % mod
        return dp[h]    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        h = int(input())
        
        ob = Solution()
        print(ob.countBT(h))
# } Driver Code Ends