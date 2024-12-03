# Non Repeating Character
# Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
# Note: When you return '$' driver code will output -1.

# Examples:

# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: In the given string, 'f' is the first character in the string which does not repeat.

class Solution:
    # Function to find the first non-repeating character in a string
    def non_repeating_char(self, s: str) -> str:
        s_map = {}
        
        # Count the frequency of each character in the string
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1
        
        # Find the first character with a frequency of 1
        for ch in s:
            if s_map[ch] == 1:
                return ch
        
        # Return '$' if no non-repeating character is found
        return '$'

# Input from the user
s = input("Enter the string: ")

solution = Solution()
result = solution.non_repeating_char(s)

if result != '$':
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found.")
