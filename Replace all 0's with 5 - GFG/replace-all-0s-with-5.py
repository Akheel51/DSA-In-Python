# Function should return an integer value
def convertFive(n):
    s=str(n)
    res=""
    for i in s:
        if i=="0":
            res+="5"
        else:
            res+=i
    return int(res)


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends