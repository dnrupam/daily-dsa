# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

class RemoveDuplicates:
    def function_name(self, nums):
        lst = {}
        for num in nums:
            lst[num] = lst.get(num, 0) + 1

        for i, j in lst.items():
            if lst[i] > 1:
                return True
        return False

obj = RemoveDuplicates()
print(obj.function_name([1, 2, 3, 4, 3, 5, 5]))


# time and space complexity: o(n) & o(n)
# pattern used: hashmap