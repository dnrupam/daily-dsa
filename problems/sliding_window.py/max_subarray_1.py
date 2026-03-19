# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])
        max_avg = window_sum
        

        for i in range(k, n):
            window_sum = (window_sum - nums[i-k] + nums[i])
            max_avg = max(max_avg, window_sum)
        return max_avg/k



nums = [7,4,5,8,8,3,9,8,7,6]
k = 7
obj = Solution()
print(obj.findMaxAverage(nums, k))
