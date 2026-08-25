#74.Search a 2D Matrix
from ast import List


def searchMatrix(matrix, target):
    m,n = len(matrix),len(matrix[0])
    left,right = 0,m*n-1
    while left <= right:
        mid = (left + right) // 2
        row,col = mid // n,mid % n
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            right = mid - 1
        else:
            left = mid + 1
        return False

#240. Search a 2D Matrix II
def searchMatrix( matrix: List[List[int]], target: int) -> bool:
    m , n = len(matrix),len(matrix[0])
    r,c = 0,n-1
    while r < m and c >= 0:
        if target == matrix[r][c]:
            return True
        elif target < matrix[r][c]:
            c -= 1
        else:
            r += 1
    return False

#378. Kth Smallest Element in a Sorted Matrix