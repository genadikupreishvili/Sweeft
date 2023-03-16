def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    matrix = [[0] * c for _ in range(r)]
    for i in range(r):
        matrix[i] = list(grid[i])
    newMatrix = [['O'] * c for _ in range(r)]
    newMatrix2 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            newMatrix[i][j] = 'O'
            newMatrix2[i][j] = 'O'

    if n % 2 == 1:
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 'O':
                    newMatrix[i][j] = '.'
                    if i - 1 >= 0:
                        newMatrix[i - 1][j] = '.'
                    if i + 1 < r:
                        newMatrix[i + 1][j] = '.'
                    if j - 1 >= 0:
                        newMatrix[i][j - 1] = '.'
                    if j + 1 < c:
                        newMatrix[i][j + 1] = '.'

        for i in range(r):
            for j in range(c):
                if newMatrix[i][j] == 'O':
                    newMatrix2[i][j] = '.'
                    if i - 1 >= 0:
                        newMatrix2[i - 1][j] = '.'
                    if i + 1 < r:
                        newMatrix2[i + 1][j] = '.'
                    if j - 1 >= 0:
                        newMatrix2[i][j - 1] = '.'
                    if j + 1 < c:
                        newMatrix2[i][j + 1] = '.'
    if n == 1:
        return [''.join(row) for row in matrix]
    elif n % 4 == 1:
        return [''.join(row) for row in newMatrix2]
    else:
        return [''.join(row) for row in newMatrix]
