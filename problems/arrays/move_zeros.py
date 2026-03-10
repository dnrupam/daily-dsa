# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Example 3:
# Input: nums = [0, 1]
# Output: [1, 0]

class Solution:
    def moveZeros(self, nums): 
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:  #[0,1,0,3,12]
                nums[j] = nums[i] 
                j += 1
        
        for i in range(j, n):
            nums[i] = 0
        return nums


nums = [0]
obj = Solution()
print(obj.moveZeros(nums))


class Solution2:
    def moveZeros(self, nums): 
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]  
                slow += 1
        return nums

nums = [0,1,0,3,12]
obj = Solution2()
print(obj.moveZeros(nums))