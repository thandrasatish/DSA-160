# Problem Name : - Equilibrium Point
# Difficulty : - Easy

# Description: -

# Given an array of integers arr[], the task is to find the first equilibrium point in the array.

# The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

# Input: arr[] = [1, 2, 0, 3]
# Output: 2 
# Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
# Input: arr[] = [1, 1, 1, 1]
# Output: -1
# Explanation: There is no equilibrium index in the array.
# Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
# Output: 3
# Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.


def findEquilibrium(arr):
    n = len(arr)
    total_sum = sum(arr)
    prefix_sum = 0 

    for i in range(n):
        if((total_sum-prefix_sum-arr[i]) == (prefix_sum)):
            return i

        prefix_sum += arr[i]

    return -1




arr = [2,1,0,3]
print(findEquilibrium(arr))