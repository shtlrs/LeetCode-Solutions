class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        shift_number= 0
        while shift_number < len(s):
            s= s[1:] + s[0]
            if s == goal:
                return True
            shift_number+=1
        return False