# Move All Zeros to End

# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.

# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.

class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        n = len(arr)
        
        # Iterate through the array
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]  # Swap non-zero element with the count index
                count += 1  # Move the count pointer

def main():
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    solution = Solution()
    solution.pushZerosToEnd(arr)
    
    # Print the modified array
    print("Array after moving zeros to the end:", ' '.join(map(str, arr)))

if __name__ == "__main__":
    main()
