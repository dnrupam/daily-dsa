# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        
        for i in t:
            d2[i] = d2.get(i, 0) + 1
    
        return d1 == d2


s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))



from collections import Counter

class Solution2:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict
    


s = "cat"
t = "dog"
obj = Solution2()
print(obj.isAnagram(s, t))