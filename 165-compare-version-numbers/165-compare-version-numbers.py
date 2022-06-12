class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        dot = "."
        version1 = list(map(int, version1.split(dot)))
        version2 = list(map(int, version2.split(dot)))
        n2 = len(version2)
        n1 = len(version1)
        m = max(n1, n2)
        if n2 > n1:
            version1.extend([0] * (n2 - n1))
        elif n1 > n2:
            version2.extend([0] * (n1 - n2))
            
        
        for i in range(m):
            if version1[i] > version2[i]:
                return 1
            elif version2[i] > version1[i]:
                return -1
            
        
        return 0