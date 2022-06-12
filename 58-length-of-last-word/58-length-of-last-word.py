class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_words = s.strip().split(" ")
        
        return len(split_words[-1])