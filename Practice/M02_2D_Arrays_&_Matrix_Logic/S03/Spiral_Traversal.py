#54.Spiral Matrix Traversal
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        top,bottom = 0,rows - 1
        left,right = 0,cols - 1
        res = []
        while top <= bottom and left <= right:
            for c in range(left,right+1):
                res.append(matrix[top][c])
            top += 1
            #top to bottom
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

           
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

           
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res

#59.Spiral Matrix II
def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                res[top][c] = num
                num += 1
            top += 1

            for r in range(top, bottom + 1):
                res[r][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res[bottom][c] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res[r][left] = num
                    num += 1
                left += 1

        return res