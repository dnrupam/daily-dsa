# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, s: str) -> str:
        char_list = list(s)
        vowels = "aeiouAEIOU"

        left = 0
        right = len(char_list) - 1

        while left < right:

            while left < right and char_list[left] not in vowels:
                left += 1
            
            while left < right and char_list[right] not in vowels:
                right -= 1
            
            if left < right:
                char_list[left],  char_list[right]= char_list[right], char_list[left]

                left += 1
                right -= 1
        
        return "".join(char_list)
            

s = "leetcode"
obj = Solution()
print(obj.reverseVowels(s))