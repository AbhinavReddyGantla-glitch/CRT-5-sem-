#48.Rotate Image
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

#1886. Determine Whether Matrix Can Be Obtained By Rotation
def findRotation(mat, target):
    for _ in range(4):
        if mat == target:
            return True
        mat = rotate(mat)
    return False

