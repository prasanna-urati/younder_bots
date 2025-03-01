def subset(arr, target_sum):
    n = len(arr)
    
    
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    
    for i in range(n + 1):
        dp[i][0] = True  
    
    
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
               
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                
            else:
            
                dp[i][j] = dp[i - 1][j]
    

    return dp[n][target_sum]

arr1 = [3, 34, 4, 12, 5, 2]
sum1 = 9
print(subset(arr1, sum1)) 

arr2 = [3, 34, 4, 12, 5, 2]
sum2 = 30
print(subset(arr2, sum2))