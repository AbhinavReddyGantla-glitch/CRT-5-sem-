def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Sort diagonals starting from the first column
    for start_row in range(rows):
        diagonal = []
        r = start_row
        c = 0

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r = start_row
        c = 0
        i = 0

        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    # Sort diagonals starting from the top row
    for start_col in range(1, cols):
        diagonal = []
        r = 0
        c = start_col

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r = 0
        c = start_col
        i = 0

        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []

    for i in range(m):
        mat.append(list(map(int, input().split())))

    print(diagonalSort(mat))