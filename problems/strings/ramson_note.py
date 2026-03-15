# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for key, value in r_count.items():
            if r_count[key] > m_count.get(key, 0):
                return False
        return True

# problem understanding, we need to make ransomnote from magazine, 
# so to make a i need to look in magszine whether I have it or not, if not than False

#logic-----

# so if the count of character in ransomnote is higher than the count of character in magazine, return false
# that means magazine has less count of char, that I need to make ramsone
# now if it has than true
