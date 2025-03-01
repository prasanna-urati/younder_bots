def permute(nums):
    def back(path, remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            
            if i > 0 and remaining[i] == remaining[i-1]:
                continue
        
            back(path + [remaining[i]], remaining[:i] + remaining[i+1:])
    
    nums.sort() 
    result = []
    back([], nums)
    return result

print(permute([1, 1, 2]))
print(permute([1, 2, 3]))