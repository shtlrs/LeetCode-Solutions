class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        s_dict = {}
        
        differences = []
        
        length = len(s)
        goal_length = len(goal)
        
        if length != goal_length:
            return False
        
        for index in range(length):
            
            if s[index] in s_dict:
                s_dict[s[index]] += 1
            else:
                s_dict[s[index]] = 1
            
            if s[index] !=  goal[index]:
                
                differences.append((s[index], goal[index]))
        
        
        if differences == []:

            for char in s_dict:
                if s_dict[char] > 1:
                    return True
                
            return False
            
        if len(differences) == 2:
            if differences[0] == tuple(reversed(differences[1])):
                return True
            else:
                return False
            
        return False
