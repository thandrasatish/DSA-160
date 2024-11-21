// Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

// Note: The second largest element should not be equal to the largest element.

// Input: arr[] = [12, 35, 1, 10, 34, 1]
// Output: 34
// Explanation: The largest element of the array is 35 and the second largest element is 34.

// Input: arr[] = [10, 5, 10]
// Output: 5
// Explanation: The largest element of the array is 10 and the second largest element is 5.

// Input: arr[] = [10, 10, 10]
// Output: -1
// Explanation: The largest element of the array is 10 and the second largest element does not exist.

class Solution:
    def getSecondLargest(self, arr):
        # Initialize first and second to negative infinity
        first = second = float('-inf')
        
        for i in arr:
            # Update first and second if a new largest element is found
            if i > first:
                second = first
                first = i
            # Update second if a new second largest element is found
            elif i > second and i < first:
                second = i
        
        # If second is still negative infinity, return -1 indicating no second largest
        if second == float('-inf'):
            return -1
        return second

# Driver code to take input and output the result
if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    
    sol = Solution()
    result = sol.getSecondLargest(arr)
    
    if result == -1:
        print("There is no second largest element.")
    else:
        print("The second largest element is:", result)
