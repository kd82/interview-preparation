from collections import List
def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isFirstRow, isFirstCol = False, False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0: isFirstRow = True
                    if j == 0: isFirstCol = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if isFirstRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if isFirstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0