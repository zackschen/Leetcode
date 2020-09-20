class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []

        if 0 == len(matrix) or 0 == len(matrix[0]): return

        m = len(matrix)
        n = len(matrix[0])


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)

        for i in range(m):
            for j in range(n):
                if i in row or j in column:
                    matrix[i][j] = 0
        print(matrix)

print(Solution().setZeroes([
]))