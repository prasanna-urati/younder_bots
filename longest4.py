def longest(arr, K):
    left = 0
    current_sum = 0
    mlength = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        
        while current_sum > K:
            current_sum -= arr[left]
            left += 1
        
    
        mlength = max(mlength, right - left + 1)
    
    return mlength

arr = [3, 1, 2, 1, 4, 5]
K = 7
print(longest(arr, K)) 