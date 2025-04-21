def max_circular_subarray_sum(arr):
    n = len(arr)
    total_sum = 0
    
    max_sum =0
    min_sum = 0
    max_total_sum = float('-inf')
    min_total_sum = float('inf')
    
    for i in range(n):
        max_sum = max(max_sum + arr[i], arr[i])
        max_total_sum = max(max_total_sum,max_sum)
        
        min_sum  = min(min_sum+arr[i],arr[i])
        
        min_total_sum = min(min_total_sum,min_sum)
        
        total_sum += arr[i]
        
    if(total_sum == min_total_sum):
        return min_total_sum
    circular_sum = total_sum - min_total_sum
    
    return max(circular_sum,max_total_sum)
    
    
    


arr = [8, -8, 9, -9, 10, -11, 12]
arr1 = [10, -3, -4, 7, 6, 5, -4, -1]
arr2 = [-1, 40, -14, 7, 6, 5, -4, -1]
print(max_circular_subarray_sum(arr))
print(max_circular_subarray_sum(arr1))
print(max_circular_subarray_sum(arr2))