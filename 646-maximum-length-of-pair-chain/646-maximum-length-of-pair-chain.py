class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda interval: interval[1])
        start = pairs[0]
        n_pairs = len(pairs)
        result = [start]
        for i in range(1, n_pairs):
            if pairs[i][0] > start[1]:
                result.append(pairs[i])
                start = pairs[i]
        
        return len(result)