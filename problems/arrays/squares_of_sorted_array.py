# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# def sortedSquares(nums):
#     nums = [num*num for num in nums]
#     return sorted(nums)

# print(sortedSquares([-4,-1,0,3,10]))

def sortedSquares(nums):    
    left = 0
    right = len(nums) -1

    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left]**2)
            left += 1
        else:
            result.append(nums[right]**2)
            right -= 1
    result.reverse()
    return result
print(sortedSquares([-4,-1,0,3,10]))