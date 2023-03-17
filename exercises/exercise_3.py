def bomberMan(n, grid):
    # Calculate number of rows and columns of grid
    r = len(grid)
    c = len(grid[0])

    # Create a matrix to represent the initial state of the grid
    matrix = [[0] * c for _ in range(r)]
    for i in range(r):
        matrix[i] = list(grid[i])

    # Create two matrices to represent the state of the grid after 1 and 2 seconds, respectively
    newMatrix = [['O'] * c for _ in range(r)]
    newMatrix2 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            newMatrix[i][j] = 'O'
            newMatrix2[i][j] = 'O'

    # If n is odd, update the state of newMatrix to represent the state of the grid after 1 second,
    # and update the state of newMatrix2 to represent the state of the grid after 2 seconds
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

    # If n is 1, return the initial state of the grid
    elif n == 1:
        return [''.join(row) for row in matrix]

    # If n is not divisible by 4, return the state of the grid after 1 second
    elif n % 4 != 0:
        return [''.join(row) for row in newMatrix]

    # If n is divisible by 4, return the state of the grid after 2 seconds
    else:
        return [''.join(row) for row in newMatrix2]
