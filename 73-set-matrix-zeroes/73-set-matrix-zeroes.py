class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        target_rows = set()
        target_cols = set()
        
        for row_index, row in enumerate(matrix):
            for col_index, cell in enumerate(row):
                if cell == 0:
                    target_rows.add(row_index)
                    target_cols.add(col_index)
                    
        for row_index, row in enumerate(matrix):
            if row_index in target_rows:
                row = [0] * n_cols
                matrix[row_index] = row
            for col_index, cell in enumerate(row):
                if col_index in target_cols:
                    matrix[row_index][col_index] = 0