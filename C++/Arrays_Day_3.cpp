// Reverse an Array
// Difficulty: EasyAccuracy: 55.32%Submissions: 72K+Points: 2
// You are given an array of integers arr[]. Your task is to reverse the given array.

// Examples:

// Input: arr = [1, 4, 3, 2, 6, 5]
// Output: [5, 6, 2, 3, 4, 1]
// Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> reverseArray(vector<int>& arr) {
        int n = arr.size();        // Get the size of the array
        int n1 = n / 2;            // Find the midpoint
        int i = 0;                 // Initialize the index
        
        // Loop to swap elements
        while (i < n1) {
            swap(arr[i], arr[n - i - 1]); // Swap elements
            i++;                          // Increment the index
        }
        return arr;
    }
};

int main() {
    Solution solution;
    
    // Test case
    vector<int> inputArray = {1, 2, 3, 4, 5};
    cout << "Original Array: ";
    for (int num : inputArray) {
        cout << num << " ";
    }
    cout << endl;
    
    // Reverse the array
    vector<int> reversedArray = solution.reverseArray(inputArray);
    
    cout << "Reversed Array: ";
    for (int num : reversedArray) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
