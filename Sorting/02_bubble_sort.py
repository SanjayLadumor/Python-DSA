# Problem: Insertion Sort
# Time Complexity: O(n²)
# Space Complexity: O(1)

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

nums = [5,2,4,6,1,3]

print(bubble_sort(nums))