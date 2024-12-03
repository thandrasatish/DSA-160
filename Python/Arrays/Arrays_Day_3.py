# Reverse an Array
# Difficulty: EasyAccuracy: 55.32%Submissions: 72K+Points: 2
# You are given an array of integers arr[]. Your task is to reverse the given array.

# Examples:

# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]
# Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.



class Solution:
    def reverseArray(self, arr):
        # Calculate the length of the array
        n = len(arr)
        # Find the midpoint
        n1 = n // 2
        # Initialize the index
        i = 0
        # Loop to swap elements
        while i < n1:
            # Swap the elements
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
            # Move to the next index
            i += 1
        return arr

# Example usage
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()
    
    # Test the reverseArray function
    input_array = [1, 2, 3, 4, 5]
    print("Original Array:", input_array)
    
    # Reverse the array
    reversed_array = solution.reverseArray(input_array)
    print("Reversed Array:", reversed_array)
