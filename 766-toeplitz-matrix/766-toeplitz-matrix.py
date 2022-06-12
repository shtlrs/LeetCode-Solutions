class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        for i in range(n_rows-1):
            for j in range(n_cols-1): 
                if matrix[i][j]!= matrix[i+1][j+1]:
                        return False
        return True