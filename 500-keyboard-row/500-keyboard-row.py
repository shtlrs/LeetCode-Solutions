class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        result = []
        
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        
        for word in words:
            word_to_lower = word.lower()
            all_in_first = [char in first_row for char in word_to_lower]
            if all(all_in_first):
                result.append(word)
                continue
            
            all_in_second = [char in second_row for char in word_to_lower]
            if all(all_in_second):
                result.append(word)
                continue
            
            all_in_third = [char in third_row for char in word_to_lower]
            if all(all_in_third):
                result.append(word)
                continue
        return result