# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        q = Queue()
        q.put([root])

        while not q.empty():
            
            nodes = q.get()
            tmp_nodes = []
            tmp_results = []
            
            for node in nodes:
                if node:
                    tmp_nodes.append(node.left)
                    tmp_nodes.append(node.right)
                    tmp_results.append(node.val)
            
            if tmp_nodes:
                q.put(tmp_nodes)
            if tmp_results:
                result.append(tmp_results)
        
        return result
        
            