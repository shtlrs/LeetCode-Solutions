class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_values = {
            "R": 0,
            "L": 0,
            "U": 0,
            "D": 0,
        }
        for move in moves:
            moves_values[move] += 1
        return moves_values["R"] == moves_values["L"] and moves_values["U"] == moves_values["D"]
                