// Rotate Array
// Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

// Note: Consider the array as circular.
// Examples :

// Input: arr[] = [1, 2, 3, 4, 5], d = 2
// Output: [3, 4, 5, 1, 2]
// Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
  public:
    // Function to rotate an array by d elements in counter-clockwise direction.
    void rotateArr(vector<int>& arr, int d) {
        int n = arr.size();

        // Ensure that d is within the range of the array's size
        d = d % n;

        // Step 1: Reverse the first d elements
        reverse(arr.begin(), arr.begin() + d);

        // Step 2: Reverse the remaining elements from d to n
        reverse(arr.begin() + d, arr.end());

        // Step 3: Reverse the whole array to get the final rotated array
        reverse(arr.begin(), arr.end());
    }
};

// Main function to test the solution
int main() {
    Solution sol;
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    int d = 2;

    // Rotate the array
    sol.rotateArr(arr, d);

    // Output the rotated array
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
