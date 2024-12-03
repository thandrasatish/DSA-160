// Kadane's Algorithm
// Given an integer array arr[]. You need to find the maximum sum of a subarray.

// Examples:

// Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
// Output: 11
// Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
// Input: arr[] = [-2, -4]
// Output: -2
// Explanation: The subarray {-2} has the largest sum -2.
// Input: arr[] = [5, 4, 1, 7, 8]
// Output: 25
// Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to find the sum of the contiguous subarray with maximum sum.
    int maxSubarraySum(vector<int> &arr) {
        int res = arr[0];
        int currMax = arr[0];

        // Traverse the array starting from the second element
        for (int i = 1; i < arr.size(); i++) {
            currMax = max(currMax + arr[i], arr[i]);
            res = max(res, currMax); 
        }

        return res;
    }
};

int main() {
    // Example usage
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4}; // Sample input
    Solution obj;
    int maxSum = obj.maxSubarraySum(arr);
    cout << "Maximum contiguous subarray sum is: " << maxSum << endl;
    return 0;
}
