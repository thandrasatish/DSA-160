# Anagram
# Difficulty: EasyAccuracy: 44.93%Submissions: 362K+Points: 2
# Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

# Note: You can assume both the strings s1 & s2 are non-empty.

# Examples :

# Input: s1 = "geeks", s2 = "kseeg"
# Output: true
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

from collections import Counter

def are_anagrams(s1: str, s2: str) -> bool:
    # Count the frequency of characters in both strings
    s1_map = Counter(s1)
    s2_map = Counter(s2)
    
    # Check if the frequency distributions are the same
    return s1_map == s2_map

# Input strings from the user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Call the function and print the result
if are_anagrams(s1, s2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
