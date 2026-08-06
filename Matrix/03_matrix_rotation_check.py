# Problem: Determine if Matrix Can Rotate to Target
# Approach: Rotate 90 degrees repeatedly
# Time Complexity: O(n²)
# Space Complexity: O(1)

def MatrixRotation(matrix,target):
    if matrix==target:
        return True
    for i in range(0,3):
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j],matrix[i][j]
        if matrix==target:
            return True
    return False

print(MatrixRotation([[0, 0, 0], [0, 1, 0], [1, 1, 1]],[[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
print(MatrixRotation([[0, 1], [1, 1]],[[1, 0], [0, 1]]))