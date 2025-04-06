# Largest Subarray of Zeros and Ones
# Difficulty Level: Easy 
# Given an array of 0s and 1s, the task is to find the length of the longest subarray with an equal number of 0s and 1s

# Input: arr[] = [0, 1, 0, 1, 0, 1]
# Output: 6   
# Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

# Input: arr[] = [0, 0, 1, 1, 0]
# Output: 4
# Explnation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.

# Input: arr[] = [0]
# Output: 0
# Explnation: There is no subarray with an equal number of 0s and 1s.



def largestSubarrayWithZerosOnes(arr):
    n = len(arr)
    prefix_sum = 0 
    d = {}
    ans = 0
    for i in range(n):
        # Convert 0 to -1
        arr[i] = -1 if arr[i] == 0 else 1
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            ans = max(ans, i + 1)
        
        if prefix_sum in d:
            ans = max(ans, i - d[prefix_sum])
        else:
            d[prefix_sum] = i
    return ans

arr = [0, 1, 0, 1, 0, 1]
print(largestSubarrayWithZerosOnes(arr))  # Output: 6
arr = [0, 0, 1, 1, 0]
print(largestSubarrayWithZerosOnes(arr))  # Output: 4
