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

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int getSecondLargest(vector<int>& arr) {
        int first = INT_MIN;
        int second = INT_MIN;
        
        int n = arr.size();
        
        for (int i = 0; i < n; i++) {
            if (arr[i] > first) {
                second = first;
                first = arr[i];
            }
            else if (arr[i] > second && arr[i] < first) {
                second = arr[i];
            }
        }
        
        return second == INT_MIN ? -1 : second;
    }
};

int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    
    vector<int> arr(n);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    Solution sol;
    int result = sol.getSecondLargest(arr);
    
    if (result == -1) {
        cout << "There is no second largest element." << endl;
    } else {
        cout << "The second largest element is: " << result << endl;
    }
    
    return 0;
}
