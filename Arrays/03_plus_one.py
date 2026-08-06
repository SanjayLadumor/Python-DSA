# Problem: Plus One
# Approach: Array Traversal
# Time Complexity: O(n)
# Space Complexity: O(1)

def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

digits = [9,9,9]

print(plusOne(digits))