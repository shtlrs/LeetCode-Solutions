from string import digits, ascii_letters

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        s = s.lower()
        s = "".join([char for char in s if char in digits or char in ascii_letters]) 
        j = len(s) - 1
        
        i = 0
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            return False
        
        return True