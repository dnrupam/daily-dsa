class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) -1 

        while left < right:

            if numbers[left] + numbers[right] > target:
                right -= 1
        
        return left

                

numbers = [2, 7, 11, 15] 
target = 9

obj = Solution()
print(obj.twoSum(numbers, target))