class Solution:
    def isPalindrome(self, x):
        text = str(x)
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False

            left += 1
            right -= 1

        return True


x = 121
obj = Solution()
print(obj.isPalindrome(x))


class Solution:
    def isPalindrome(self, x):
        text = str(x)
        left = 0
        right = len(text) -1

        while left < right:
            if text[left] != text[right]:
                return False
            left += 1
            left -= 1
        return True