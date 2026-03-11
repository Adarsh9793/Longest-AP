# Given an array of integers, find the length of the longest arithmetic progression in it.
def longestAP(arr):
    if len(arr) == 0:
        return 0
    
    dp = [[1 for i in range(100)] for j in range(len(arr)+1)]

    ans = 1
    for i in range(1,len(arr)):
        for j in range(i):
            diff = arr[i] - arr[j]
            dp[i][diff] = 1 + dp[j][diff]
            ans = max(ans, dp[i][diff])

    return ans

arr = [1,7,10,13,14,19]
print(longestAP(arr))