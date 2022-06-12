class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        fs = []
        ss = []
        
        for char in s:
            if char != "#":
                fs.append(char)
            else:
                if fs:
                    fs.pop()
                
        for char in t:
            if char != "#":
                ss.append(char)
            else:
                if ss:
                    ss.pop()
                        
        return fs == ss