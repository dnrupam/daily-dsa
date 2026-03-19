# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        seen = set()
        n = len(s)

        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            length = max(length, i-left + 1)
        return length

s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))