class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        count = 0
        for i in range(n):
            l, r = i+1, n-1
            while l<r:
                curSum = arr[i]+arr[l]+arr[r]
                if curSum < sumo:
                    count += r-l
                    l += 1
                elif curSum >= sumo:
                    r -= 1
        return count
                
    
#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends