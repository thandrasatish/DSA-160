// Move All Zeros to End

// Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

// Examples:

// Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
// Output: [1, 2, 4, 3, 5, 0, 0, 0]
// Explanation: There are three 0s that are moved to the end.

// Input: arr[] = [10, 20, 30]
// Output: [10, 20, 30]
// Explanation: No change in array as there are no 0s.

// Input: arr[] = [0, 0]
// Output: [0, 0]
// Explanation: No change in array as there are all 0s.

#include <iostream>
#include <vector>
#include <algorithm> // for swap function

using namespace std;

class Solution {
public:
    void pushZerosToEnd(vector<int>& arr) {
        int count = 0;
        int n = arr.size();
        
        // Iterate through the array
        for(int i = 0; i < n; i++) {
            if(arr[i] != 0) {
                swap(arr[i], arr[count]); // Swap non-zero element with the count index
                count++; // Move the count pointer
            }
        }
    }
};

int main() {
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;

    vector<int> arr(n);
    
    cout << "Enter the elements of the array: ";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    solution.pushZerosToEnd(arr);
    
    // Print the modified array
    cout << "Array after moving zeros to the end: ";
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
