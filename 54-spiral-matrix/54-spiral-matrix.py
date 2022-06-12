
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n_rows = len(matrix)
        n_columns = len(matrix[0])
        spiral = []
        visited = set()

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

        counter = 0

        x = 0
        y = 0

        while len(spiral) != n_rows * n_columns:

            if (0 > x
                    or x >= n_columns
                    or 0 > y
                    or y>= n_rows
                    or (x, y) in visited):
                x -= dx[counter % 4]
                y -= dy[counter % 4]
                counter += 1
                x += dx[counter % 4]
                y += dy[counter % 4]
            else:
                spiral.append(matrix[y][x])
                visited.add((x, y))
                x += dx[counter % 4]
                y += dy[counter % 4]

        return spiral

