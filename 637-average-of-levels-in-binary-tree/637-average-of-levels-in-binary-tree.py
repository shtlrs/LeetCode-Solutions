# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []
        
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            level = []
            
            for i in range(size):
                node = queue.pop(0)
                
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                
            results.append(sum(level) / len(level))
        
        
        return results