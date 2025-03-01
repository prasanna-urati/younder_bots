def string(input):
    r = []
    i = 0
    while i < len(input):
        char = input[i] 
        j = i + 1
        
        while j < len(input) and input[j].isdigit():
            j += 1
        
        
        count = int(input[i + 1:j]) if j > i + 1 else 1
        r.append(char * count)
        
        i = j  
    
    return ''.join(r)

input = input("Enter the string: ")


print(string(input))
