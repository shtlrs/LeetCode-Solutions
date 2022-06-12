from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_to_sets = ["".join(sorted(word)) for word in strs]
        s = defaultdict(list)
        print(strs_to_sets)
        for index, element in enumerate(strs_to_sets):
            s[element].append(index)
            
        result = []
        for key in s:
            sub_result = []
            anagram_indices = s[key]
            for index in anagram_indices:
                sub_result.append(strs[index])
            result.append(sub_result)
        
        return result
        