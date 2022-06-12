class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s = [char for char in s]
        j = len(s) -1 
        i = 0
        
        while i < j:
            if s[i].lower() not in vowels:
                i += 1
                continue
            if s[j].lower() not in vowels:
                j -= 1
                continue
                
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
                
            
        return "".join(s)