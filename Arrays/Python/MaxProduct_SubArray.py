def maxium_product_subarray(arr):
    left_to_right = 1 
    max_prod = float('-inf')
    n = len(arr)
    
    for i in range(n):
        if(left_to_right == 0):
            left_to_right = 1 
        
        left_to_right *= arr[i]
        max_prod = max(max_prod,left_to_right)
    
    right_to_left = 1 
    
    for i in range(n-1,-1,-1):
        if(right_to_left == 0):
            right_to_left = 1 
        
        right_to_left *= arr[i]
        max_prod = max(max_prod,right_to_left)
    return max_prod


arr = [-2,6,-3,-10,0,2]
print(maxium_product_subarray(arr))
    