class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        n = len(s)
        for i in range(n):
            s[i] = s[i][::-1]
            
        return " ".join(s)