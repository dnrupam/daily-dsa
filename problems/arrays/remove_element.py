nums = [0,1,0,3,12]
val = 0

def removeElement(nums, val):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != val: # i = 1, nums[1] != 3 --> 2 != 3
            nums[j] = nums[i] # nums[0] = nums[1] --> 3 = 2 ---> [2,2,2,3]
            j += 1 # j becomes 1 after first iteration
    return j, nums
print(removeElement(nums, val))