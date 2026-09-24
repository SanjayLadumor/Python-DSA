# Question :
# Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix,target):
    rows = len(matrix)
    cols = len(matrix[0])
    start = 0
    end = rows * cols - 1
    while start <= end:
        mid = (start + end) // 2
        row = mid // cols
        col = mid % cols
        if matrix[row][col] == target:
            return True

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))