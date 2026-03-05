# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums, target):
        n = len(nums) # 3
        for i in range(n):  # 0,1,2
            for j in range(i+1, n): #1,3
                if nums[i] + nums[j] == target: # num[0] + num[1] == 6 --> 3 + 2 == 5 
                                                # num[0] + num[2] == 6 --> 3 + 4 == 7
                                                # num[1] + num[2] == 6 --> 2 _ 4 == 6
                    return [i,j]
        return []



nums = [3,3]
target = 6
obj = Solution()
print(obj.twoSum(nums, target))