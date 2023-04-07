#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        res=""
        for i in S:
            if len(res)==0 or res[-1]!=i:
                res+=i
        return res       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends