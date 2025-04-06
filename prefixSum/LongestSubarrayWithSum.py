def longestSubarrayWithSumK(arr, k):
    n = len(arr)
    prefix_sum = 0 
    d = {}
    ans = 0
    
    # Iterate through the array
    for i in range(n):
        # Update the prefix sum
        prefix_sum += arr[i]
        
        # Check if the prefix sum is equal to the target sum k
        # If true, the subarray from the beginning to the current index has the sum k
        if prefix_sum == k:
            ans = max(ans, i + 1)
        
        # Check if there is any prefix sum that when subtracted from the current prefix sum gives k
        # If true, it means there exists a subarray with sum k ending at the current index
        if (prefix_sum - k) in d:
            ans = max(ans, i - d[prefix_sum - k])
        
        # Store the first occurrence of the prefix sum in the dictionary
        # This helps in identifying the longest subarray with the desired sum
        if prefix_sum not in d:
            d[prefix_sum] = i
    
    return ans

# Test cases
arr = [10, 5, 2, 7, 1, -10]
k = 15
print(longestSubarrayWithSumK(arr, k))  # Output: 6