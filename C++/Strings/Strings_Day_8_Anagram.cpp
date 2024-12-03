// Anagram
// Difficulty: EasyAccuracy: 44.93%Submissions: 362K+Points: 2
// Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

// Note: You can assume both the strings s1 & s2 are non-empty.

// Examples :

// Input: s1 = "geeks", s2 = "kseeg"
// Output: true
// Explanation: Both the string have same characters with same frequency. So, they are anagrams.

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

bool areAnagrams(string s1, string s2) {
    if (s1.length() != s2.length()) return false; // Early exit if lengths differ

    unordered_map<char, int> char_count;

    // Increment for s1 and decrement for s2
    for (int i = 0; i < s1.length(); i++) {
        char_count[s1[i]]++;
        char_count[s2[i]]--;
    }

    // If any character count is not zero, they're not anagrams
    for (auto it : char_count) {
        if (it.second != 0) {
            return false;
        }
    }

    return true;
}

int main() {
    string s1, s2;
    
    // Input strings from the user
    cout << "Enter the first string: ";
    cin >> s1;
    cout << "Enter the second string: ";
    cin >> s2;

    // Call the function and print the result
    if (areAnagrams(s1, s2)) {
        cout << "The strings are anagrams of each other." << endl;
    } else {
        cout << "The strings are not anagrams of each other." << endl;
    }

    return 0;
}
