    # Problem: Intersection of Two Arrays
# Approach: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

def intersection(nums1, nums2):
    result = []
    for i in nums1:
        if i in nums2 and i not in result:
            result.append(i)
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1,nums2))