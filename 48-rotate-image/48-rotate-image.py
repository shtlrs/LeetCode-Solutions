def exract_and_reverse_col(matrix, col_number):
        col = []
        for row in matrix:
            col.append(row[col_number])
        col.reverse()
        return col

class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        for i in range(len(matrix)):
            cols.append(exract_and_reverse_col(matrix, i))
        
        for i in range(len(cols)):
            matrix[i] = cols[i]
        
            
        