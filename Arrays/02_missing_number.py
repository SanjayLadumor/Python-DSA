# Problem: Missing Number
# Approach: Sum Formula
# Time Complexity: O(n)
# Space Complexity: O(1)

def missingNumber(nums):
    n = len(nums)
    total = n * (n+1)//2
    for i in nums:
        total -= i
    return total

nums = [3,0,1]

print(missingNumber(nums))