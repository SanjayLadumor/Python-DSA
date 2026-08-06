# Problem: Pascal Triangle
# Approach: Previous Row Calculation
# Time Complexity: O(n²)
# Space Complexity: O(n²)

def generate(numRows):
    result = []
    for i in range(numRows):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result

print(generate(5))