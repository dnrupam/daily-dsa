# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# first would be get the count of each char and store in a hash dict, 
# then if any value is 1 return that index of it or else return -1.

class Solution:
    def firstUniqChar(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        for key in d:
            if d[key] == 1:
                return s.index(key)
        return -1
        
obj = Solution()
print(obj.firstUniqChar('leetcode'))

# time complexity is o(n2)

# more optimized

class Solution2:
    def firstUniqChar(self, s):
        d = {}
        
        for char in s:
            d[char] = d.get(char, 0) + 1  # {a:2, b:2}
        
        print(d)
        for i, char in  enumerate(s): # {0:a, 1:b}
            if d[char] == 1: 
                return i
        return -1
            
obj = Solution2()
print(obj.firstUniqChar('dddccdbba'))


from collections import Counter

class Solution3:
    def firstUniqChar(self, s: str) -> int:
        """
        Find the first non-repeating character in a string and return its index.
        If it doesn't exist, return -1.
      
        Args:
            s: Input string to search for first unique character
          
        Returns:
            Index of first unique character, or -1 if none exists
        """
        # Count frequency of each character in the string
        char_count = Counter(s)
        print(char_count)
        # Iterate through string to find first character with count of 1
        for index, char in enumerate(s):
            print(index, char)
            if char_count[char] == 1:
                return index
      
        # No unique character found
        return -1


obj = Solution3()
print(obj.firstUniqChar('dddccdbba'))