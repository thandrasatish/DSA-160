// Non Repeating Character
// Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
// Note: When you return '$' driver code will output -1.

// Examples:

// Input: s = "geeksforgeeks"
// Output: 'f'
// Explanation: In the given string, 'f' is the first character in the string which does not repeat.

#include <iostream>
#include <map>
#include <string>
using namespace std;

class Solution {
public:
    // Function to find the first non-repeating character in a string.
    char nonRepeatingChar(string &s) {
        map<char, int> s_map;
        
        // Count the frequency of each character in the string
        for (auto ch : s) {
            s_map[ch]++;
        }
        
        // Find the first character with a frequency of 1
        for (auto ch : s) {
            if (s_map[ch] == 1) {
                return ch;
            }
        }
        
        // Return '$' if no non-repeating character is found
        return '$';
    }
};

int main() {
    string s;
    cout << "Enter the string: ";
    cin >> s;

    Solution solution;
    char result = solution.nonRepeatingChar(s);

    if (result != '$') {
        cout << "The first non-repeating character is: " << result << endl;
    } else {
        cout << "No non-repeating character found." << endl;
    }

    return 0;
}
