#867.Transpose Matrix
from ast import List


def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]

        return res

#566.Reshape the Matrix
def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat

        res = [[0] * c for _ in range(r)]
        for i in range(rows * cols):
            res[i // c][i % c] = mat[i // cols][i % cols]

        return res