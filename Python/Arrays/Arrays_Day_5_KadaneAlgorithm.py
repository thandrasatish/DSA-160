# Kadane's Algorithm
# Given an integer array arr[]. You need to find the maximum sum of a subarray.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray {-2} has the largest sum -2.
# Input: arr[] = [5, 4, 1, 7, 8]
# Output: 25



class Solution:
    # Function to find the sum of the contiguous subarray with maximum sum
    def maxSubarraySum(self, arr):
        res = arr[0] 
        curr_max = arr[0] 

        for i in range(1, len(arr)):
            curr_max = max(curr_max + arr[i], arr[i]) 
            res = max(res, curr_max) 

        return res

# Example usage
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Sample input
    obj = Solution()
    max_sum = obj.maxSubarraySum(arr)
    print("Maximum contiguous subarray sum is:", max_sum)
