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
print(obj.firstUniqChar('aabb'))