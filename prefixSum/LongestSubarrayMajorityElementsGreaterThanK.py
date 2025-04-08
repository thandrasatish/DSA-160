# Longest Subarray having Majority Elements Greater Than K
# Difficulty: Medium
# Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k.
# Examples:

# Input: arr[]= [1, 2, 3, 4, 1], k = 2
# Output: 3 
# Explanation: The subarray [2, 3, 4] or [3, 4, 1] satisfy the given condition, and there is no subarray of length 4 or 5 which will hold the given condition, so the answer is 3.

# Input: arr[] = [6, 5, 3, 4], k = 2
# Output: 4
# Explanation: In the subarray [6, 5, 3, 4], there are 4 elements > 2 and 0 elements <= 2, so it is the longest subarray.

def longestSubarray(arr, k):
    n = len(arr)
    prefIdx = {}
    sum = 0
    res = 0

    for i in range(n):
        sum += 1 if arr[i] > k else -1
        if sum not in prefIdx:
            prefIdx[sum] = i
            
    if -n in prefIdx:
        return 0
    prefIdx[-n] = n

    for i in range(-n + 1, n + 1):
        if i not in prefIdx:
            prefIdx[i] = prefIdx[i - 1]
        else:
            prefIdx[i] = min(prefIdx[i], prefIdx[i - 1])

    sum = 0
    for i in range(n):
        sum += 1 if arr[i] > k else -1
        if sum > 0:
            res = i + 1
        else:
        	res = max(res, i - prefIdx[sum - 1])

    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 1]
    k = 2
    print(longestSubarray(arr, k))