def sort(arr):
    
    odd = []
    even = []
    
    for num in arr:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    
   
    odd.sort()  
    even.sort(reverse=True) 
    
   
    result = []
    oddi = 0
    eveni = 0
    
    for num in arr:
        if num % 2 == 0:
            result.append(even[eveni])
            eveni += 1
        else:
            result.append(odd[oddi])
            oddi += 1
    
    return result

arr1 = [5, 8, 11, 6, 2, 1, 7]
arr2 = [9, 4, 3, 10, 15, 2]

print(sort(arr1)) 
print(sort(arr2)) 