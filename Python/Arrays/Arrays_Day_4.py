# Rotate Array
# Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.
# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)

        # Ensure that d is within the range of the array's size
        d = d % n

        # Step 1: Reverse the first d elements
        arr[:d] = reversed(arr[:d])

        # Step 2: Reverse the remaining elements from d to n
        arr[d:] = reversed(arr[d:])

        # Step 3: Reverse the whole array to get the final rotated array
        arr.reverse()

# Main function to test the solution
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2

    # Rotate the array
    sol.rotateArr(arr, d)

    # Output the rotated array
    print(" ".join(map(str, arr)))
