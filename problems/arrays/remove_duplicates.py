class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

obj = Solution()
print(obj.removeDuplicates([0,0,1,1]))