# Problem: Move Zeroes
# Approach: Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return nums

nums = [0,1,0,3,12]

print(moveZeroes(nums))